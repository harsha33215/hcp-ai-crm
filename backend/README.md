
# Backend

The backend is developed using FastAPI and PostgreSQL.

It exposes REST APIs for interaction management and integrates LangGraph with Groq to process user conversations and extract structured healthcare interaction data.

## Features

- CRUD APIs
- AI Chat API
- Interaction extraction
- Search interactions
- Follow-up generation
- Insights generation

## Run

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Swagger:

```
http://localhost:8000/docs
```
