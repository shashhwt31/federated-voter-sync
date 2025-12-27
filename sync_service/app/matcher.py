from common.scoring import score_match

# Stores last-seen hashes by state
seen_hashes = {}

# Stores detected duplicates
matches = []

def process_event(event: dict):
    state = event["state"]
    hashes = event["hashes"]

    for other_state, other_hashes in seen_hashes.items():
        if other_state != state and other_hashes == hashes:
            confidence = score_match(True)
            matches.append({
                "state_1": other_state,
                "state_2": state,
                "hash": hashes,
                "confidence": confidence
            })

    # Record this event
    seen_hashes[state] = hashes
