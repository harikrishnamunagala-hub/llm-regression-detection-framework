from fastapi import FastAPI
from app import main

app = FastAPI(
    title="LLM Regression Detection Framework",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "LLM Regression Detection Framework API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/evaluate")
def evaluate():
    results = main()
    return results