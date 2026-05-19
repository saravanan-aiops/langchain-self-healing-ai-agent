from fastapi import FastAPI
from app.agents.incident_agent import analyze_incident
from app.agents.remediation_agent import remediate
from app.agents.verification_agent import verify

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Self Healing AI Agent Running"
    }

@app.post("/heal")
def heal(logs: str):

    analysis = analyze_incident(logs)

    remediation = remediate(analysis)

    verification = verify()

    return {
        "analysis": analysis,
        "remediation": remediation,
        "verification": verification
    }