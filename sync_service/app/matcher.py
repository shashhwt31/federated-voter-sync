from common.scoring import score_match

seen_hashes = {}

def match_event(event):
    matches = []
    for state, hashes in seen_hashes.items():
        if hashes == event["hashes"]:
            confidence = score_match(True)
            matches.append((state, confidence))
    seen_hashes[event["state"]] = event["hashes"]
    return matches
