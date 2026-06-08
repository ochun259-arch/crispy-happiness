from langchain_core.tools import tool

from app.db.expense_repository import add_expense_item, list_recent_expenses


@tool
def add_expense(amount: float, category: str, description: str = "") -> str:
    """记录一笔生活支出。当用户说花了钱、记账、记录消费时使用。

    Args:
        amount: 金额（元）
        category: 分类，如餐饮、交通、购物、娱乐、其他
        description: 可选备注
    """
    if amount <= 0:
        return "金额必须大于 0。"
    expense_id = add_expense_item(amount, category, description)
    detail = f"{category} {amount:.2f} 元"
    if description.strip():
        detail += f"（{description.strip()}）"
    return f"已记录支出 #{expense_id}：{detail}"


@tool
def list_expenses(limit: int = 10) -> str:
    """列出最近的支出记录。当用户询问花了多少钱、查看账单、消费记录时使用。

    Args:
        limit: 返回条数，默认 10 条
    """
    limit = max(1, min(limit, 50))
    expenses = list_recent_expenses(limit)
    if not expenses:
        return "当前没有支出记录。"
    lines = []
    total = 0.0
    for item in expenses:
        total += item["amount"]
        desc = f"，{item['description']}" if item["description"] else ""
        lines.append(
            f"{item['id']}. {item['category']} {item['amount']:.2f} 元"
            f"{desc}（{item['created_at']}）"
        )
    return f"最近 {len(expenses)} 笔支出（合计 {total:.2f} 元）：\n" + "\n".join(lines)
