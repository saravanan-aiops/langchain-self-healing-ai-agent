from app.tools.shell_tool import run_command

def remediate(issue):

    if "CrashLoopBackOff" in issue:

        return run_command("echo Restarting deployment")

    return {"message": "No remediation found"}