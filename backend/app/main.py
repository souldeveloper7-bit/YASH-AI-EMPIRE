
from fastapi import FastAPI

app = FastAPI(
    title="YASH AI EMPIRE",
    description="Central AI Control System",
    version="1.0.0"
)

@app.get("/")
async def home():
    return {
        "project": "YASH AI EMPIRE",
        "status": "online",
        "message": "Central AI Backend is running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
