import uuid
import requests
from common.normalization import normalize_identity
from common.hashing import hash_value
from app.config import STATE_CODE, STATE_SALT, SYNC_URL

def emit_event(voter):
    identity = normalize_identity(voter.name, voter.dob)
    hashed = hash_value(identity, STATE_SALT)

    event = {
        "event_id": str(uuid.uuid4()),
        "state": STATE_CODE,
        "event_type": "REGISTER_OR_UPDATE",
        "hashes": {
            "name_dob": hashed
        }
    }

    requests.post(f"{SYNC_URL}/events", json=event)
