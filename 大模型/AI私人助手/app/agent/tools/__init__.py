from app.agent.tools.expense_tools import add_expense, list_expenses
from app.agent.tools.income_tools import add_income, list_incomes
from app.agent.tools.preference_tools import save_preference, search_preferences
from app.agent.tools.todo_tools import add_todo, list_todos
from app.agent.tools.weather_tools import get_weather

ALL_TOOLS = [
    add_todo,
    list_todos,
    add_expense,
    list_expenses,
    add_income,
    list_incomes,
    get_weather,
    save_preference,
    search_preferences,
]

__all__ = [
    "add_todo",
    "list_todos",
    "add_expense",
    "list_expenses",
    "add_income",
    "list_incomes",
    "get_weather",
    "save_preference",
    "search_preferences",
    "ALL_TOOLS",
]
