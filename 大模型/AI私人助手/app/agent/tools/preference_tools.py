from langchain_core.tools import tool

from app.rag.bootstrap import create_preference
from app.rag.preference_index import get_preference_vector_store


@tool
def save_preference(content: str) -> str:
    """保存一条个人生活偏好或习惯。当用户要求记住偏好、爱好、习惯时使用。

    示例：「我不吃香菜」「我的爱好是看书」「我习惯晚上11点睡觉」。
    注意：具体待办任务应使用 add_todo，不要使用本工具。
    """
    content = content.strip()
    if not content:
        return "偏好内容不能为空。"
    preference = create_preference(content)
    return f"已保存偏好 #{preference['id']}：{preference['content']}"


@tool
def search_preferences(query: str) -> str:
    """搜索已保存的个人偏好、爱好和习惯。当用户询问偏好、爱好、习惯时使用。

    示例：「我有什么爱好？」「我不吃什么？」「我的习惯是什么？」。
    注意：待办任务应使用 list_todos，不要使用本工具。
    """
    query = query.strip()
    if not query:
        return "请提供要搜索的内容。"

    documents = get_preference_vector_store().search(query, k=3)
    if not documents:
        return "没有找到相关的偏好记录。"

    lines = []
    for index, doc in enumerate(documents, start=1):
        record_id = doc.metadata.get("record_id", "未知")
        lines.append(f"{index}. [偏好 #{record_id}] {doc.page_content}")
    return "相关偏好：\n" + "\n".join(lines)
