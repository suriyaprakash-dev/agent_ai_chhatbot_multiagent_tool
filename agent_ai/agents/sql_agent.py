from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
# from config import GEMINI_API_KEY, MODEL_NAME
from config import GROQ_API_KEY,MODEL_NAME
from langchain_groq import ChatGroq
from agents.ll import llm
from tools.sql_tool import sql_agent

# ==========================
# LLM
# ==========================

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

# ==========================
# Memory
# ==========================

memory = MemorySaver()

# ==========================
# SQL Agent
# ==========================

sql_agent = create_react_agent(
    model=llm,
    tools=[sql_agent],
    checkpointer=memory
)