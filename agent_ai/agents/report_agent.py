from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
# from config import GEMINI_API_KEY, MODEL_NAME
from langchain_openai import ChatOpenAI
from agents.ll import llm
from config import GROQ_API_KEY,MODEL_NAME
from langchain_groq import ChatGroq
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)
report_agent = create_react_agent(
    model=llm,
    tools=[]
)