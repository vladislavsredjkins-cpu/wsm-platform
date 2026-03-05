from fastapi import FastAPI, Query

app = FastAPI(title="World Strongman Platform API", version="1.0.0")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ranking")
def get_ranking(
    division: str = Query("MEN"),
    format: str = Query("CLASSIC"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    # временная заглушка — важно, чтобы endpoint существовал
    return {
        "division": division,
        "format": format,
        "limit": limit,
        "offset": offset,
        "items": []
    }
    @app.get("/__build")
def __build():
    return {"service": "wsm-platform-backend", "build": "RANKING_V1"}
