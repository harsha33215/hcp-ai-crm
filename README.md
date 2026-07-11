# HCP AI CRM Assistant

This project was built as part of an AI Healthcare CRM assignment.

The goal is to help medical representatives record doctor interactions more efficiently using AI. Instead of manually filling every field, the user can describe the meeting in plain English, and the AI extracts the important details such as the doctor's name, hospital, meeting summary, and follow-up actions.

The extracted information can then be reviewed, edited if required, and saved to the database.

---

## Features

- AI-powered interaction logging
- Automatic extraction of meeting details
- Create, update, delete, and view interactions
- Search interactions
- Generate follow-up emails
- Generate AI insights
- Simple and responsive user interface

---

## Tech Stack

### Frontend

- React
- Vite
- Material UI
- Axios

### Backend

- FastAPI
- PostgreSQL
- SQLAlchemy
- LangGraph
- Groq LLM

---

## Project Structure

```
hcp-ai-crm
│
├── backend
├── frontend
└── README.md
```

---

## Running the Project

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## API Documentation

After starting the backend, Swagger is available at

```
http://localhost:8000/docs
```

---

## Demo

A demo video of the project is available here:

> Add your video link after uploading.

---

## About

This project was developed to demonstrate how AI can simplify interaction logging in a Healthcare CRM system by combining FastAPI, LangGraph, Groq, PostgreSQL, and React into a complete full-stack application.
