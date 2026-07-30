from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GROQ_API_KEY,MODEL_NAME
from langchain_groq import ChatGroq
from agents.ll import llm
from langchain_openai import ChatOpenAI
from tools.pdf_tool import pdf_tool

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
# PDF Agent
# ==========================

pdf_agent = create_react_agent(
    model=llm,
    tools=[pdf_tool],
    checkpointer=memory
)