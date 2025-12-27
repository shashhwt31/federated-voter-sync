from fastapi import APIRouter
from app.matcher import match_event
from app.audit import log_event

router = APIRouter()

@router.post("/events")
def receive_event(event: dict):
    log_event(event)
    matches = match_event(event)
    return {
        "matches": matches
    }

@router.get("/audit")
def audit():
    return {"events": log_event}
