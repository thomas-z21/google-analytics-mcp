import os
if "GA_KEY_JSON" in os.environ:
    with open("/app/credentials.json", "w") as f:
        f.write(os.environ["GA_KEY_JSON"])

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Ensure analytics-mcp is installed once on startup
os.system('pipx install analytics-mcp || true')

@app.route("/run_report", methods=["POST"])
def run_report():
    payload = request.json or {}
    property_id = payload.get("property_id", "")

    # Compose and run the analytics-mcp command directly
    cmd = ["analytics-mcp", "run_report", property_id]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return jsonify({
        "command": cmd,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
