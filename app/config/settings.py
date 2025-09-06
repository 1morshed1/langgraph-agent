from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")

    ALLOWED_MODEL_NAMES = [
        "llama-3.3-70b-versatile",
        "openai/gpt-oss-120b"
    ]

settings = Settings()