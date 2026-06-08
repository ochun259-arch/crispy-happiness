import pickle
from typing import Callable

import faiss
import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from app.config import settings
from app.rag.embeddings import get_embeddings


class FaissVectorStore:
    def __init__(self, index_name: str) -> None:
        self.index_name = index_name
        self._store: FAISS | None = None

    @property
    def is_empty(self) -> bool:
        return self._store is None

    def load_or_create(self, load_records: Callable[[], list[dict]]) -> None:
        index_dir = settings.faiss_index_path
        faiss_path = index_dir / f"{self.index_name}.faiss"
        pkl_path = index_dir / f"{self.index_name}.pkl"
        if faiss_path.exists() and pkl_path.exists():
            with open(faiss_path, "rb") as file:
                index = faiss.deserialize_index(
                    np.frombuffer(file.read(), dtype=np.uint8)
                )
            with open(pkl_path, "rb") as file:
                docstore, index_to_docstore_id = pickle.load(file)
            self._store = FAISS(
                get_embeddings(),
                index,
                docstore,
                index_to_docstore_id,
            )
            return

        records = load_records()
        if records:
            self.rebuild_from_records(records)

    def rebuild_from_records(self, records: list[dict]) -> None:
        if not records:
            self.clear()
            return
        documents = [
            Document(
                page_content=record["content"],
                metadata={
                    "record_id": record["id"],
                    "created_at": record["created_at"],
                },
            )
            for record in records
        ]
        self._store = FAISS.from_documents(documents, get_embeddings())
        self.save()

    def add_record(self, record_id: int, content: str, created_at: str) -> None:
        document = Document(
            page_content=content,
            metadata={"record_id": record_id, "created_at": created_at},
        )
        if self._store is None:
            self._store = FAISS.from_documents([document], get_embeddings())
        else:
            self._store.add_documents([document])
        self.save()

    def search(self, query: str, k: int = 3) -> list[Document]:
        if self._store is None:
            return []
        return self._store.similarity_search(query, k=k)

    def clear(self) -> None:
        self._store = None
        index_dir = settings.faiss_index_path
        for suffix in (".faiss", ".pkl"):
            path = index_dir / f"{self.index_name}{suffix}"
            if path.exists():
                path.unlink()

    def save(self) -> None:
        if self._store is None:
            return
        index_dir = settings.faiss_index_path
        index_dir.mkdir(parents=True, exist_ok=True)
        faiss_path = index_dir / f"{self.index_name}.faiss"
        pkl_path = index_dir / f"{self.index_name}.pkl"

        serialized = faiss.serialize_index(self._store.index)
        with open(faiss_path, "wb") as file:
            if isinstance(serialized, np.ndarray):
                file.write(serialized.tobytes())
            else:
                file.write(bytes(serialized))
        with open(pkl_path, "wb") as file:
            pickle.dump((self._store.docstore, self._store.index_to_docstore_id), file)
