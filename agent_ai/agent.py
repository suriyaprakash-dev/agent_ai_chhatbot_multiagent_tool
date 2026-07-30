# from langchain_google_genai import ChatGoogleGenerativeAI
# from tools.web_tool import google_search
# from langgraph.prebuilt import create_react_agent
# from langgraph.checkpoint.memory import MemorySaver
# from tools.pdf_tool import pdf_tool
# from tools.weather_tool import weather
# from config import GEMINI_API_KEY
# from config import MODEL_NAME
# from tools.sql_tool import sql_agent

# from tools.calculator_tool import calculator

# # ==========================
# # Gemini LLM
# # ==========================
# llm = ChatGoogleGenerativeAI(
#     model=MODEL_NAME,
#     api_key=GEMINI_API_KEY,
#     temperature=0
# )

# # ==========================
# # Memory
# # ==========================
# memory = MemorySaver()

# # ==========================
# # Agent
# # ==========================
# agent = create_react_agent(
#     model=llm,
#     tools=[
#         calculator,
#         google_search,
#         pdf_tool,
#         weather,
#         sql_agent
#     ],
#     checkpointer=memory
# )