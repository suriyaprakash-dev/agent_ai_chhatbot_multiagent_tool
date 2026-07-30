from agents.ll import llm
from collaboration import collaborate
from config import GROQ_API_KEY, MODEL_NAME
from agents.math_agent import math_agent
from agents.pdf_agent import pdf_agent
from agents.sql_agent import sql_agent
from agents.weather_agent import weather_agent
from agents.web_agent import web_agent
from langchain_groq import ChatGroq
# llm = ChatGoogleGenerativeAI(
#     model=MODEL_NAME,
#     api_key=GEMINI_API_KEY,
#     temperature=0
# )
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

SYSTEM_PROMPT = """
You are a Supervisor Agent.

Choose ONLY ONE route.

math
- calculations

pdf
- summarize PDF
- explain PDF
- answer questions only from uploaded PDF

sql
- employee database
- salary
- attendance
- performance
- attrition

weather
- weather
- forecast

web
- latest news
- internet search

collaboration
- compare PDF with database
- employees mentioned in PDF
- salary of employees in PDF
- attendance of employees in PDF
- performance of employees in PDF
- PDF + SQL
- PDF + Web
- use multiple agents

Return ONLY ONE WORD.

math
pdf
sql
weather
web
collaboration
"""

def supervisor(question):

    response = llm.invoke(
        SYSTEM_PROMPT + "\n\nQuestion:\n" + question
    )

    route = response.content.lower().strip()

    print("Supervisor Selected:", route)

    if route == "math":
        return math_agent

    elif route == "pdf":
        return pdf_agent

    elif route == "sql":
        return sql_agent

    elif route == "weather":
        return weather_agent

    elif route == "collaboration":
        return collaborate

    else:
        return web_agent