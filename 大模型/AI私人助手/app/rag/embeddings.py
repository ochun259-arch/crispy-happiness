from functools import lru_cache

from langchain_community.embeddings import HuggingFaceEmbeddings

from app.config import settings


@lru_cache
def get_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        encode_kwargs={"normalize_embeddings": True},
    )
