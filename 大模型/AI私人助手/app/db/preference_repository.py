from app.db.database import get_connection


def add_preference_item(content: str) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO preferences (content) VALUES (?)",
            (content.strip(),),
        )
        conn.commit()
        return cursor.lastrowid


def get_preference_by_id(preference_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, content, created_at FROM preferences WHERE id = ?",
            (preference_id,),
        ).fetchone()
    return dict(row) if row else None


def list_preferences(limit: int = 50) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, content, created_at
            FROM preferences
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]


def get_all_preferences() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, content, created_at
            FROM preferences
            ORDER BY id ASC
            """
        ).fetchall()
    return [dict(row) for row in rows]
