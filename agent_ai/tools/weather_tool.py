from langchain.tools import tool

from tools.web_tool import groq_search


@tool
def weather(location: str) -> str:
    """
    Get the current weather for a city or location.

    Examples:
    Chennai
    Coimbatore
    New York
    London
    """

    query = f"Current weather in {location}"

    return groq_search.invoke(query)