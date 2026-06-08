from langchain_core.tools import tool

from app.db.income_repository import add_income_item, list_recent_incomes


@tool
def add_income(amount: float, category: str, description: str = "") -> str:
    """记录一笔收入。当用户说收到钱、发工资、入账、有收入时使用。

    Args:
        amount: 金额（元）
        category: 分类，如工资、奖金、兼职、理财、其他
        description: 可选备注
    """
    if amount <= 0:
        return "金额必须大于 0。"
    income_id = add_income_item(amount, category, description)
    detail = f"{category} {amount:.2f} 元"
    if description.strip():
        detail += f"（{description.strip()}）"
    return f"已记录收入 #{income_id}：{detail}"


@tool
def list_incomes(limit: int = 10) -> str:
    """列出最近的收入记录。当用户询问收入、入账、赚了多少钱时使用。

    Args:
        limit: 返回条数，默认 10 条
    """
    limit = max(1, min(limit, 50))
    incomes = list_recent_incomes(limit)
    if not incomes:
        return "当前没有收入记录。"
    lines = []
    total = 0.0
    for item in incomes:
        total += item["amount"]
        desc = f"，{item['description']}" if item["description"] else ""
        lines.append(
            f"{item['id']}. {item['category']} {item['amount']:.2f} 元"
            f"{desc}（{item['created_at']}）"
        )
    return f"最近 {len(incomes)} 笔收入（合计 {total:.2f} 元）：\n" + "\n".join(lines)
