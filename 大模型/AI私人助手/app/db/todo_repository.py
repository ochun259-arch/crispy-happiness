from app.db.database import get_connection


def add_todo_item(content: str) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO todos (content) VALUES (?)",
            (content.strip(),),
        )
        conn.commit()
        return cursor.lastrowid


def list_pending_todos() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, content, created_at
            FROM todos
            WHERE completed = 0
            ORDER BY id ASC
            """
        ).fetchall()
    return [dict(row) for row in rows]
