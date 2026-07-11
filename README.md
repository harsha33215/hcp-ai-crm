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



How to Test the Application
Once both the backend and frontend are running, open the application and try the following steps.

1. Test AI Interaction Extraction
Open the AI Assistant and paste the following message:

Met Dr. John Smith at Apollo Hospital today.

We discussed our new diabetes medication and its clinical trial results. The doctor was interested in prescribing it for suitable patients and requested product samples along with the latest clinical study documents.

I agreed to send the samples next Monday and schedule a follow-up meeting after two weeks.
The AI will extract the interaction details and automatically populate the interaction form.

Review the extracted information and click Save to store it in the database.

2. Test Another Interaction
Visited Dr. Priya Sharma at Fortis Hospital.

We discussed the latest hypertension treatment guidelines and introduced our cardiovascular product portfolio. She requested dosage recommendations and patient education brochures.

Follow up next Friday with additional marketing material.

---

## About

This project was developed to demonstrate how AI can simplify interaction logging in a Healthcare CRM system by combining FastAPI, LangGraph, Groq, PostgreSQL, and React into a complete full-stack application.
