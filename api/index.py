from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class Payload(BaseModel):
    regions: list[str]
    threshold_ms: int

@app.post("/analyze")
async def analyze(payload: Payload):
    return {"message": "working"}
