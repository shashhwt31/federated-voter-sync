from pydantic import BaseModel
from typing import Dict

class Event(BaseModel):
    event_id: str
    state: str
    event_type: str
    hashes: Dict[str, str]

class MatchNotification(BaseModel):
    event_id: str
    matched_state: str
    confidence: float
