from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.services.groq_service import ask_llm, extract_interaction


def log_interaction_tool(user_input: str, db: Session):

    data = extract_interaction(user_input)

    interaction = Interaction(
    hcp_name=data.get("hcp_name", "Unknown"),
    hospital=data.get("hospital", ""),
    meeting_type=data.get("meeting_type", "Meeting"),

    discussion=user_input,

    topics_discussed=data.get("topics_discussed", ""),
    materials_shared=data.get("materials_shared", ""),
    samples_distributed=data.get("samples_distributed", ""),
    sentiment=data.get("sentiment", ""),
    outcomes=data.get("outcomes", ""),
    follow_up_actions=data.get("follow_up_actions", ""),

    summary=data.get("summary", ""),
    action_items=data.get("action_items", ""),

    created_by_ai=True
)

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "tool": "log_interaction",
        "message": "Interaction logged successfully",
        "interaction": {
            "id": interaction.id,
            "hcp_name": interaction.hcp_name,
            "hospital": interaction.hospital,
            "meeting_type": interaction.meeting_type,
            "summary": interaction.summary,
            "action_items": interaction.action_items
        }
    }


def edit_interaction_tool(
    interaction_id: int,
    new_message: str,
    db: Session
):

    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return {
            "error": "Interaction not found"
        }

    interaction.discussion = new_message

    interaction.summary = ask_llm(
        f"Summarize professionally:\n{new_message}"
    )

    db.commit()
    db.refresh(interaction)

    return {
        "tool": "edit_interaction",
        "message": "Interaction Updated",
        "interaction": {
            "id": interaction.id,
            "summary": interaction.summary
        }
    }


from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.services.groq_service import ask_llm


def search_interaction_tool(
    user_input: str,
    db: Session
):

    prompt = f"""
Extract ONLY the doctor's name from the following text.

Examples:
Input: Search Dr. John
Output: Dr. John

Input: Find Dr. Sarah
Output: Dr. Sarah

Input: Show interactions with Dr. Kumar
Output: Dr. Kumar

Return ONLY the doctor's name.

Input:
{user_input}
"""

    hcp_name = ask_llm(prompt).strip()

    results = db.query(Interaction).filter(
        Interaction.hcp_name.ilike(f"%{hcp_name}%")
    ).all()

    response = []

    for item in results:
        response.append({
            "id": item.id,
            "hcp_name": item.hcp_name,
            "hospital": item.hospital,
            "meeting_type": item.meeting_type,
            "summary": item.summary,
            "action_items": item.action_items
        })

    return response

def followup_tool(message: str):

    prompt = f"""
Write a professional follow-up email for the following HCP interaction.

Interaction:

{message}
"""

    return ask_llm(prompt)


def insights_tool(message: str):

    prompt = f"""
You are a Healthcare CRM AI.

Analyze this interaction.

Return:

1. Customer Interest
2. Recommended Next Action
3. Sales Opportunity
4. Risk Level

Interaction:

{message}
"""

    return ask_llm(prompt)