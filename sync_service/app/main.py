from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Voter Sync Service")
app.include_router(router)
