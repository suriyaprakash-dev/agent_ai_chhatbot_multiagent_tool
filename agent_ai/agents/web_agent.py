from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.ll import llm
# from config import GEMINI_API_KEY, MODEL_NAME
from tools.web_tool import groq_search

# ==========================
# LLM
# ==========================

from langchain_openai import ChatOpenAI
# from config import GROK_API_KEY


# ==========================
# Memory
# ==========================

memory = MemorySaver()

# ==========================
# Web Agent
# ==========================

web_agent = create_react_agent(
    model=llm,
    tools=[groq_search],
    checkpointer=memory
)