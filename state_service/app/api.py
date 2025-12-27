from fastapi import APIRouter
from app.models import Voter
from app.database import voters, notifications
from app.events import emit_event

router = APIRouter()

@router.post("/register")
def register_voter(voter: Voter):
    voters[voter.voter_id] = voter
    emit_event(voter)
    return {"status": "registered"}

@router.get("/voters")
def list_voters():
    return voters

@router.get("/notifications")
def get_notifications():
    return notifications
