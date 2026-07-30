from langchain.tools import tool
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)


@tool
def groq_search(query: str) -> str:
    """
    Answer general knowledge questions using the Groq LLM.
    Note: This does NOT perform live web search.
    """

    try:
        response = llm.invoke(query)
        return response.content

    except Exception as e:
        return f"Error: {e}"