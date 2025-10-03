from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/run_report", methods=["POST"])
def run_report():
    payload = request.json or {}
    property_id = payload.get("property_id", "")
    result = subprocess.run(
        ["pipx", "run", "analytics-mcp", "run_report", property_id], 
        capture_output=True, text=True
    )
    return jsonify({"output": result.stdout, "error": result.stderr})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
