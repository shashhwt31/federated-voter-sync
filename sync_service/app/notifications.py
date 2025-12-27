import requests

def notify_state(state_url, payload):
    requests.post(f"{state_url}/notifications", json=payload)
