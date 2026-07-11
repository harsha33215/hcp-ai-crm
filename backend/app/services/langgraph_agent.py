from typing import Any, Literal
from app.services.prompts import EXTRACTION_PROMPT
from langgraph.graph import END, StateGraph
import json
from app.services.state import AgentState
from app.services.prompts import INTENT_PROMPT
from app.services.groq_service import ask_llm
from app.services.tools import (
    edit_interaction_tool,
    followup_tool,
    insights_tool,
    log_interaction_tool,
    search_interaction_tool,
)
def extract_interaction_node(state: AgentState):

    user_input = state["user_input"]

    prompt = f"""
{EXTRACTION_PROMPT}

User Input:

{user_input}
"""

    result = ask_llm(prompt)

    try:
        interaction = json.loads(result)
    except Exception:
        interaction = {
            "hcp_name": "",
            "hospital": "",
            "meeting_type": "",
            "discussion": "",
            "summary": result,
            "action_items": ""
        }


    return {
        **state,
        "response": {
            "tool": "extract_interaction",
            "message": "Interaction extracted successfully",
            "interaction": interaction
        }
    }
def detect_intent(state: AgentState):

    user_input = state["user_input"]

    prompt = f"""
{INTENT_PROMPT}

User Input:

{user_input}
"""

    intent = ask_llm(prompt).strip().lower()

    valid_intents = [
        "log_interaction",
        "edit_interaction",
        "search_interaction",
        "generate_followup",
        "generate_insights"
    ]

    if intent not in valid_intents:
        intent = "generate_insights"

    return {
        **state,
        "intent": intent
    }


def route_intent(
        state: AgentState
) -> Literal[
    "log_interaction",
    "edit_interaction",
    "search_interaction",
    "generate_followup",
    "generate_insights"
]:

    return state["intent"]

def log_node(state: AgentState):

    return extract_interaction_node(state)
def edit_node(state: AgentState):
    # Demo implementation:
    # Updates interaction with ID = 1
    result = edit_interaction_tool(
        1,
        state["user_input"],
        state["db"],
    )

    return {
        **state,
        "response": result,
    }


def search_node(state: AgentState):
    result = search_interaction_tool(
        state["user_input"],
        state["db"],
    )

    return {
        **state,
        "response": result,
    }


def followup_node(state: AgentState):
    result = followup_tool(
        state["user_input"]
    )

    return {
        **state,
        "response": {
            "tool": "generate_followup",
            "content": result,
        },
    }


def insights_node(state: AgentState):
    result = insights_tool(
        state["user_input"]
    )

    return {
        **state,
        "response": {
            "tool": "generate_insights",
            "content": result,
        },
    }
graph_builder = StateGraph(AgentState)

graph_builder.add_node(
    "detect_intent",
    detect_intent
)

graph_builder.add_node(
    "log_interaction",
    log_node
)

graph_builder.add_node(
    "edit_interaction",
    edit_node
)

graph_builder.add_node(
    "search_interaction",
    search_node
)

graph_builder.add_node(
    "generate_followup",
    followup_node
)

graph_builder.add_node(
    "generate_insights",
    insights_node
)

graph_builder.set_entry_point(
    "detect_intent"
)

graph_builder.add_conditional_edges(
    "detect_intent",
    route_intent,
    {
        "log_interaction": "log_interaction",
        "edit_interaction": "edit_interaction",
        "search_interaction": "search_interaction",
        "generate_followup": "generate_followup",
        "generate_insights": "generate_insights",
    }
)

graph_builder.add_edge(
    "log_interaction",
    END
)

graph_builder.add_edge(
    "edit_interaction",
    END
)

graph_builder.add_edge(
    "search_interaction",
    END
)

graph_builder.add_edge(
    "generate_followup",
    END
)

graph_builder.add_edge(
    "generate_insights",
    END
)

graph = graph_builder.compile()