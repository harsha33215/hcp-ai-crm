import json
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from app.services.prompts import EXTRACTION_PROMPT

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("MODEL_NAME"),
    temperature=0,
)


def ask_llm(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content


def extract_interaction(text: str):
    prompt = f"""
{EXTRACTION_PROMPT}

Conversation:

{text}
"""

    response = ask_llm(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)
    except Exception:
        return {
            "hcp_name": "Unknown",
            "hospital": "",
            "meeting_type": "Meeting",
            "topics_discussed": "",
            "materials_shared": "",
            "samples_distributed": "",
            "sentiment": "",
            "outcomes": "",
            "follow_up_actions": "",
            "summary": text,
            "action_items": ""
        }