from datetime import datetime
from pydantic import BaseModel

class InteractionBase(BaseModel):
    hcp_name: str
    hospital: str | None = None
    meeting_type: str | None = None

    discussion: str | None = None
    summary: str | None = None
    action_items: str | None = None

    topics_discussed: str | None = None
    materials_shared: str | None = None
    samples_distributed: str | None = None
    sentiment: str | None = None
    outcomes: str | None = None
    follow_up_actions: str | None = None
    attendees: str | None = None


class InteractionCreate(InteractionBase):
    pass


class InteractionUpdate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):
    id: int
    interaction_mode: str
    created_by_ai: bool
    created_at: datetime

    class Config:
        from_attributes = True