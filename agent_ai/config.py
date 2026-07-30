import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# Groq
# ==========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-120b"

# ==========================
# MySQL
# ==========================
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# ==========================
# Embedding Model
# ==========================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================
# Paths
# ==========================
UPLOAD_FOLDER = "uploads"
CHROMA_DB = "chroma_db"

TOP_K = 3