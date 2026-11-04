from fastapi import FastAPI
import requests
import os

app = FastAPI(title="AI Microservice", description="DevSecOps Pipeline Project")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/analyze")
def analyze_text(text: str):
    # We will wire up the Hugging Face API later
    api_key = os.getenv("AI_API_KEY", "dummy_key")
    if api_key == "dummy_key":
        return {"status": "warning", "message": "API key not configured yet", "input": text}
    
    return {"status": "success", "processed_text": f"Simulated AI analysis of: {text}"}
