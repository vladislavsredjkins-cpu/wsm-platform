from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="World Strongman Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "WSM API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ranking")
def ranking(division: str, format: str, limit: int = 10, offset: int = 0):
    return {
        "division": division,
        "format": format,
        "limit": limit,
        "offset": offset,
        "ranking": [
            {"athlete_id": "WSM001", "name": "Athlete 1", "points": 1200},
            {"athlete_id": "WSM002", "name": "Athlete 2", "points": 1100}
        ]
    }
