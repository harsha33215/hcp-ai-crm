from app.services.langgraph_agent import graph

result = graph.invoke(
    {
        "user_input": "Generate a follow up email for Dr John",
        "intent": "",
        "response": {}
    }
)

print(result)