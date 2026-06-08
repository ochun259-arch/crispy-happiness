from app.db.preference_repository import get_all_preferences
from app.rag.faiss_store import FaissVectorStore

_preference_store = FaissVectorStore("preferences")


def get_preference_vector_store() -> FaissVectorStore:
    return _preference_store


def bootstrap_preferences_index() -> None:
    store = get_preference_vector_store()
    records = get_all_preferences()
    if records:
        store.rebuild_from_records(records)
    else:
        store.clear()
