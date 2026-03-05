from fastapi import FastAPI

app = FastAPI(title="World Strongman Platform API")


@app.get("/")
def root():
    return {"message": "World Strongman Platform API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ranking")
def ranking(
    division: str = "MEN",
    format: str = "CLASSIC",
    limit: int = 10,
    offset: int = 0
):
    return {
        "division": division,
        "format": format,
        "limit": limit,
        "offset": offset,
        "athletes": [
            {"name": "Tom Stoltman", "country": "UK", "points": 1200},
            {"name": "Oleksii Novikov", "country": "Ukraine", "points": 1180}
        ]
    }
