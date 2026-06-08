from app.db.database import get_connection


def add_income_item(amount: float, category: str, description: str = "") -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO incomes (amount, category, description)
            VALUES (?, ?, ?)
            """,
            (amount, category.strip(), description.strip()),
        )
        conn.commit()
        return cursor.lastrowid


def list_recent_incomes(limit: int = 10) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, amount, category, description, created_at
            FROM incomes
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]
