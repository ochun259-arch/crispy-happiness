import httpx
from langchain_core.tools import tool
from urllib.parse import quote


def _fetch_weather(city: str) -> dict:
    response = httpx.get(
        f"https://wttr.in/{quote(city)}",
        params={"format": "j1", "lang": "zh"},
        timeout=15.0,
        headers={"User-Agent": "curl/8.0"},
    )
    response.raise_for_status()
    return response.json()


@tool
def get_weather(city: str) -> str:
    """查询指定城市的当前天气。当用户询问某地天气、温度、是否下雨时使用。

    Args:
        city: 城市名称，如北京、上海、广州
    """
    city = city.strip()
    if not city:
        return "请提供要查询的城市名称。"

    data = None
    for _ in range(2):
        try:
            data = _fetch_weather(city)
            break
        except httpx.HTTPError:
            continue
    if data is None:
        return f"暂时无法获取 {city} 的天气信息，请稍后再试。"

    current = data.get("current_condition", [{}])[0]
    area = data.get("nearest_area", [{}])[0]
    area_name = area.get("areaName", [{}])[0].get("value", city)

    temp = current.get("temp_C", "未知")
    feels_like = current.get("FeelsLikeC", "未知")
    humidity = current.get("humidity", "未知")
    weather_desc = current.get("lang_zh", [{}])
    if weather_desc:
        condition = weather_desc[0].get("value", "未知")
    else:
        condition = current.get("weatherDesc", [{}])[0].get("value", "未知")

    return (
        f"{area_name} 当前天气：{condition}，"
        f"气温 {temp}°C（体感 {feels_like}°C），湿度 {humidity}%。"
    )
