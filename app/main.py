from fastapi import FastAPI

from app.agents.incident_agent import analyze_incident
from app.agents.remediation_agent import remediate
from app.agents.verification_agent import verify

from app.db.memory import (
    save_incident,
    get_previous_incidents
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Self Healing AI Agent Running"
    }


@app.post("/heal")
def heal(logs: str):

    analysis = analyze_incident(logs)

    print("FINAL ANALYSIS:", analysis)

    remediation = remediate(analysis)

    verification = verify()

    save_incident(
        logs,
        analysis.get("root_cause"),
        analysis.get("remediation")
    )

    return {
        "analysis": analysis,
        "remediation": remediation,
        "verification": verification
    }


@app.get("/incidents")
def incidents():

    return {
        "incidents": get_previous_incidents()
    }