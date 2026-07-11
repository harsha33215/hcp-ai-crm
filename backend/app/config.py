from pathlib import Path
from dotenv import load_dotenv
import os

# backend folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from backend/
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemma2-9b-it")

