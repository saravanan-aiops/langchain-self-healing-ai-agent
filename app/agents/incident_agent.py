from langchain_ollama import ChatOllama
import json

llm = ChatOllama(model="phi3:mini")

def analyze_incident(logs):

    prompt = f"""
    You are an SRE AI Agent.

    Analyze the infrastructure issue.

    Return ONLY valid JSON.

    Example:
    {{
      "root_cause": "Missing environment variable",
      "severity": "HIGH",
      "remediation": "Restart deployment",
      "service": "nginx"
    }}

    Logs:
    {logs}
    """

    response = llm.invoke(prompt)

    content = response.content.strip()

    print("RAW LLM OUTPUT:")
    print(content)

    try:

        start = content.find("{")
        end = content.rfind("}") + 1

        json_content = content[start:end]

        parsed = json.loads(json_content)

        return parsed

    except Exception as e:

        print("JSON ERROR:", e)

        return {
            "root_cause": "Unknown",
            "severity": "MEDIUM",
            "remediation": "Restart deployment",
            "service": "unknown"
        }