from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.interaction import Interaction
from app.schemas.interaction_schema import (
    InteractionCreate,
    InteractionUpdate,
    InteractionResponse,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)
@router.get("/")
def get_all_interactions(db: Session = Depends(get_db)):
    return db.query(Interaction).all()
@router.post("/")
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):
    print(interaction)
    print(interaction.model_dump())

    return {"ok": True}

@router.post("/", response_model=InteractionResponse)
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):
    new_interaction = Interaction(
        hcp_name=interaction.hcp_name,
        hospital=interaction.hospital,
        meeting_type=interaction.meeting_type,

        discussion=interaction.discussion,
        summary=interaction.summary,
        action_items=interaction.action_items,

        topics_discussed=interaction.topics_discussed,
        materials_shared=interaction.materials_shared,
        samples_distributed=interaction.samples_distributed,
        sentiment=interaction.sentiment,
        outcomes=interaction.outcomes,
        follow_up_actions=interaction.follow_up_actions,
        attendees=interaction.attendees,
    )

    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    return new_interaction

@router.get("/{interaction_id}", response_model=InteractionResponse)
def get_one(interaction_id: int, db: Session = Depends(get_db)):
    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    return interaction


@router.put("/{interaction_id}", response_model=InteractionResponse)
def update_interaction(
    interaction_id: int,
    request: InteractionUpdate,
    db: Session = Depends(get_db),
):
    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    data = request.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction


@router.delete("/{interaction_id}")
def delete_interaction(
    interaction_id: int,
    db: Session = Depends(get_db),
):
    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    db.delete(interaction)
    db.commit()

    return {"message": "Deleted successfully"}



