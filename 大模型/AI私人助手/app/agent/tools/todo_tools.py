from langchain_core.tools import tool

from app.db.todo_repository import add_todo_item, list_pending_todos


@tool
def add_todo(content: str) -> str:
    """添加一条待办任务。仅用于需要完成的具体事项（如买东西、提醒、约会）。

    注意：个人偏好、习惯、爱好应使用 save_preference，不要使用本工具。
    """
    content = content.strip()
    if not content:
        return "待办内容不能为空。"
    todo_id = add_todo_item(content)
    return f"已添加待办 #{todo_id}：{content}"


@tool
def list_todos() -> str:
    """列出未完成的待办任务。仅当用户明确询问待办、任务、要做的事时使用。

    注意：用户询问偏好、爱好、习惯时，应使用 search_preferences，不要使用本工具。
    """
    todos = list_pending_todos()
    if not todos:
        return "当前没有未完成的待办事项。"
    lines = [
        f"{item['id']}. {item['content']}（创建于 {item['created_at']}）"
        for item in todos
    ]
    return "未完成待办：\n" + "\n".join(lines)
