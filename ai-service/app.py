from flask import Flask, request, jsonify
from middleware import sanitize_input, detect_prompt_injection
from services.groq_client import call_groq
from datetime import datetime

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json.get("text", "")

    # 1. Clean input
    clean_text = sanitize_input(data)

    # 2. Check injection
    if detect_prompt_injection(clean_text):
        return jsonify({
            "status": "error",
            "message": "Prompt injection detected"
        }), 400

    # 3. Call AI
    ai_output = call_groq(clean_text)

    # 4. Return structured response
    return jsonify({
        "status": "success",
        "input": clean_text,
        "output": ai_output,
        "timestamp": datetime.utcnow().isoformat()
    })


if __name__ == "__main__":
    app.run(debug=True)