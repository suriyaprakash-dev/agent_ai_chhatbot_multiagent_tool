import pymysql
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from config import GROQ_API_KEY
from langchain_groq import ChatGroq
from config import (
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE,
    GROQ_API_KEY,
    MODEL_NAME
)

# Gemini model
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0
)

# Database schema
SCHEMA = """
Table: employee

Columns:
- id (INT)
- name (VARCHAR)
- department (VARCHAR)
- salary (INT)
- attendance (INT)
- leaves (INT)
- projects_completed (INT)
- performance_score (INT)
- attrition_risk (FLOAT)
"""


@tool
def sql_agent(question: str) -> str:
    """
    Answer HR database questions using natural language.
    Example:
    - Show all employees
    - Who has the highest salary?
    - List employees with high attrition risk
    """

    try:
        # Convert English to SQL
        prompt = f"""
You are a MySQL expert.

Database schema:
{SCHEMA}

Convert the user question into ONLY a valid MySQL query.
Do not add explanations.
Do not use markdown.

Question: {question}
SQL:
"""

        sql_query = llm.invoke(prompt).content.strip()

        # Remove accidental markdown
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

        # Connect to MySQL
        connection = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )

        cursor = connection.cursor()

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        connection.close()

        if not rows:
            return f"Generated SQL: {sql_query}\\n\\nNo records found."

        return f"Generated SQL: {sql_query}\\n\\nResults:\\n{rows}"

    except Exception as e:
        return f"Database Error: {e}"