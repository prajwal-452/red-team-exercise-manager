from flask import Blueprint, request, jsonify
from services.groq_client import generate_response
import json
from datetime import datetime

ai_bp = Blueprint("ai", __name__)

def load_prompt(file_name):
    with open(f"prompts/{file_name}", "r") as f:
        return f.read()

@ai_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    # Input validation
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    user_input = data["text"]

    if not isinstance(user_input, str) or len(user_input.strip()) == 0:
        return jsonify({"error": "Invalid input"}), 400

    try:
        #  Load prompt
        prompt_template = load_prompt("describe.txt")
        final_prompt = prompt_template.replace("{input}", user_input)

        #  Call AI
        ai_output = generate_response(final_prompt)

        # Convert AI output string → JSON
        parsed_output = json.loads(ai_output)

        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": parsed_output
        })

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid AI JSON response"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500