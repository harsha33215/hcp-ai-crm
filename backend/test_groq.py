from app.services.groq_service import ask_llm

print(
    ask_llm(
        "Reply with only: Groq Connected Successfully"
    )
)