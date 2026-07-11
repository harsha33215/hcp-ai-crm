from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.database.connection import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(255), nullable=False)

    hospital = Column(String(255))

    meeting_type = Column(String(100))

    interaction_mode = Column(String(50), default="FORM")

    # Existing
    discussion = Column(Text)
    summary = Column(Text)
    action_items = Column(Text)

    # NEW
    topics_discussed = Column(Text)

    materials_shared = Column(Text)

    samples_distributed = Column(Text)

    sentiment = Column(String(50))

    outcomes = Column(Text)

    follow_up_actions = Column(Text)

    attendees = Column(Text)

    created_by_ai = Column(Boolean, default=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )