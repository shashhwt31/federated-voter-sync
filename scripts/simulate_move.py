import requests

voter = {
    "voter_id": "123",
    "name": "Jane Doe",
    "dob": "1990-01-01",
    "address": "123 Main St"
}

requests.post("http://localhost:8001/register", json=voter)
requests.post("http://localhost:8002/register", json=voter)
