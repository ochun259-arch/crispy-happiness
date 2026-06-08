from app.db.preference_repository import add_preference_item, get_preference_by_id
from app.rag.preference_index import get_preference_vector_store


def create_preference(content: str) -> dict:
    preference_id = add_preference_item(content)
    preference = get_preference_by_id(preference_id)
    if preference is None:
        raise RuntimeError("偏好创建失败")
    get_preference_vector_store().add_record(
        preference["id"], preference["content"], preference["created_at"]
    )
    return preference


def bootstrap_rag() -> None:
    from app.rag.preference_index import bootstrap_preferences_index

    bootstrap_preferences_index()
