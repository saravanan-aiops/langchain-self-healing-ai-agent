<img width="1859" height="962" alt="image" src="https://github.com/user-attachments/assets/28dd1cd1-30a3-4c58-a2a3-a65e5f205075" />

# Self-Healing AI Agent

An Agentic AI-powered self-healing infrastructure automation platform built using LangChain, Ollama, FastAPI, and local LLMs.

This project detects infrastructure issues from logs, analyzes root causes using AI, performs automated remediation, and verifies recovery.

---

# Features

- AI-powered incident analysis
- Local LLM using Ollama
- Automated remediation workflows
- Verification agent
- FastAPI REST API
- LangChain integration
- Lightweight local setup
- GitHub portfolio ready

---

# Architecture

```text
                ┌─────────────────┐
                │   User / Alert  │
                └────────┬────────┘
                         │
                         ▼
              ┌───────────────────┐
              │ LangChain Agent   │
              └────────┬──────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    Log Analyzer   Shell Tool   Knowledge Base
          │            │            │
          ▼            ▼            ▼
     Root Cause   Auto Healing   RAG Search
          │
          ▼
    Verification Agent
          │
          ▼
      Incident Report
```

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| LangChain | AI orchestration |
| Ollama | Local LLM |
| FastAPI | REST API |
| ChromaDB | Vector database |
| LangGraph | Multi-agent workflows |
| Git | Version control |

---

# Project Structure

```bash
self-healing-ai-agent/
│
├── app/
│   ├── agents/
│   │   ├── incident_agent.py
│   │   ├── remediation_agent.py
│   │   └── verification_agent.py
│   │
│   ├── tools/
│   │   └── shell_tool.py
│   │
│   ├── utils/
│   └── main.py
│
├── data/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Local Setup (Windows 11)

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/self-healing-ai-agent.git

cd self-healing-ai-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download:

https://ollama.com/download

---

# Pull Local Models

## Lightweight LLM

```bash
ollama pull phi3:mini
```

## Embedding Model

```bash
ollama pull nomic-embed-text
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Docs

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Example

## POST `/heal`

Input:

```text
Pod nginx CrashLoopBackOff
Container restarting repeatedly
```

Example Output:

```json
{
  "analysis": "Container repeatedly failing during startup.",
  "remediation": {
    "stdout": "Restarting deployment"
  },
  "verification": {
    "stdout": "Verification completed"
  }
}
```

---

# Example Workflow

1. User submits logs
2. AI analyzes incident
3. Root cause identified
4. Auto remediation triggered
5. Verification performed
6. Incident summary returned

---

# Current Capabilities

- Log analysis
- AI incident diagnosis
- Automated shell execution
- Infrastructure verification
- FastAPI endpoints

---

# Planned Features

- Kubernetes integration
- Docker remediation
- LangGraph multi-agent workflows
- ChromaDB RAG pipeline
- CI/CD integration
- Prometheus alert ingestion
- Slack notifications
- Incident memory
- AI dashboards

---

# Security Notes

This project is intended for local development and research purposes.

Recommended production safeguards:

- Command whitelisting
- Approval workflows
- RBAC
- Audit logging
- Sandbox execution
- Rate limiting

---

# Recommended Lightweight Models

| Model | RAM Requirement |
|---|---|
| phi3:mini | ~4GB |
| tinyllama | ~2GB |
| llama3.2:1b | ~4GB |

---

# Git Commands

## Initialize Git

```bash
git init
git add .
git commit -m "Initial commit"
```

## Push to GitHub

```bash
git remote add origin YOUR_REPO_URL

git branch -M main

git push -u origin main
```

---

# Author

Ashwin Saravanan

---

# License

MIT License
