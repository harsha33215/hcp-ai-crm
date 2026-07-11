from typing import Any, TypedDict


class AgentState(TypedDict):
    user_input: str
    intent: str
    response: dict
    db: Any