from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:mini")

def analyze_incident(logs):

    prompt = f"""
    Analyze this infrastructure issue.

    Logs:
    {logs}

    Give:
    - root cause
    - severity
    - remediation
    """

    response = llm.invoke(prompt)

    return response.content