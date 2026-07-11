# Frontend

The frontend is built with React and Material UI.

It provides a simple interface where users can:

- Chat with the AI assistant
- Review extracted interaction details
- Edit information before saving
- View interaction history
- Update and delete records

## Run

```bash
npm install

npm run dev
```

The application runs on

```
http://localhost:5173
```


## How to Test the Application

Once both the backend and frontend are running, open the application and try the following steps.

### 1. Test AI Interaction Extraction

Open the **AI Assistant** and paste the following message:

```text
Met Dr. John Smith at Apollo Hospital today.

We discussed our new diabetes medication and its clinical trial results. The doctor was interested in prescribing it for suitable patients and requested product samples along with the latest clinical study documents.

I agreed to send the samples next Monday and schedule a follow-up meeting after two weeks.
```

The AI will extract the interaction details and automatically populate the interaction form.

Review the extracted information and click **Save** to store it in the database.

---

### 2. Test Another Interaction

```text
Visited Dr. Priya Sharma at Fortis Hospital.

We discussed the latest hypertension treatment guidelines and introduced our cardiovascular product portfolio. She requested dosage recommendations and patient education brochures.

Follow up next Friday with additional marketing material.
```

---

### 3. Test CRUD Operations

- Create a new interaction using the AI Assistant.
- Edit an existing interaction from the Interaction History table.
- Delete an interaction.
- Verify the changes in the table.

---

### 4. Test APIs

Swagger documentation is available at:

```
http://localhost:8000/docs
```

From Swagger, you can test:

- POST /interactions/
- GET /interactions/
- PUT /interactions/{id}
- DELETE /interactions/{id}
- POST /ai/chat

---

### Expected Workflow

1. Enter a doctor's interaction in the AI Assistant.
2. The AI extracts the important details.
3. Review the populated form.
4. Save the interaction.
5. View the saved record in the Interaction History table.
6. Edit or delete the interaction if required.
