from fastapi import APIRouter
from app.audit import events, log_event
from app.matcher import process_event, matches

router = APIRouter()

@router.post("/events")
def receive_event(event: dict):
    log_event(event)
    process_event(event)
    return {"status": "event processed"}

@router.get("/audit")
def get_audit():
    return {
        "events": events
    }

@router.get("/matches")
def get_matches():
    return {
        "duplicates_detected": matches
    }
