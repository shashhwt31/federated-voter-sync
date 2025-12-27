from pydantic import BaseModel

class Voter(BaseModel):
    voter_id: str
    name: str
    dob: str
    address: str
    status: str = "active"
