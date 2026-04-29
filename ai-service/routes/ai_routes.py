from flask import Blueprint, request, jsonify
from services.groq_client import generate_response
from services.cache import get_cached, set_cache
import json
from datetime import datetime

ai_bp = Blueprint("ai", __name__)


def load_prompt(file_name):
    with open(f"prompts/{file_name}", "r") as f:
        return f.read()


def validate_input(data):
    if not data or "text" not in data:
        return "Missing 'text' field"

    text = data["text"]

    if not isinstance(text, str) or len(text.strip()) == 0:
        return "Invalid input"

    if len(text) > 500:
        return "Input too long"

    return None


# -------------------- DESCRIBE --------------------

@ai_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    error = validate_input(data)
    if error:
        return jsonify({"error": error}), 400

    user_input = data["text"].strip()

    # limit length (ZAP safe)
    if len(user_input) > 500:
        return jsonify({"error": "Input too long"}), 400

    # prompt injection protection
    blocked_words = ["ignore previous", "system prompt", "override", "bypass"]
    if any(word in user_input.lower() for word in blocked_words):
        return jsonify({"error": "Potential prompt injection detected"}), 400
    # 🔹 Check cache
    cached = get_cached(user_input)
    if cached:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": cached,
            "cached": True
        })

    try:
        prompt_template = load_prompt("describe.txt")
        final_prompt = prompt_template.replace("{input}", user_input)

        ai_output = generate_response(final_prompt)

        if ai_output is None:
            return jsonify({"error": "AI unavailable"}), 503

        parsed_output = json.loads(ai_output)
        if "is_fallback" in parsed_output:
            return jsonify({
                "generated_at": datetime.utcnow().isoformat(),
                "data": parsed_output["data"],
                "is_fallback": True
            })
        # 🔹 Save to cache
        set_cache(user_input, parsed_output)

        # 🔹 Save to cache
        set_cache(user_input, parsed_output)

        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": parsed_output
        })

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid AI JSON response"}), 500

    except Exception:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": {
                "message": "AI service temporarily unavailable"
            },
            "is_fallback": True
        }), 200


# -------------------- RECOMMEND --------------------

@ai_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    error = validate_input(data)
    if error:
        return jsonify({"error": error}), 400

    user_input = data["text"].strip()

    # limit length (ZAP safe)
    if len(user_input) > 500:
        return jsonify({"error": "Input too long"}), 400

    # prompt injection protection
    blocked_words = ["ignore previous", "system prompt", "override", "bypass"]
    if any(word in user_input.lower() for word in blocked_words):
        return jsonify({"error": "Potential prompt injection detected"}), 400
    cached = get_cached(user_input)
    if cached:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "recommendations": cached,
            "cached": True
        })

    try:
        prompt_template = load_prompt("recommend.txt")
        final_prompt = prompt_template.replace("{input}", user_input)

        ai_output = generate_response(final_prompt)

        if ai_output is None:
            return jsonify({"error": "AI unavailable"}), 503

        parsed_output = json.loads(ai_output)
        if "is_fallback" in parsed_output:
            return jsonify({
                "generated_at": datetime.utcnow().isoformat(),
                "data": parsed_output["data"],
                "is_fallback": True
            })
        set_cache(user_input, parsed_output)

        set_cache(user_input, parsed_output)

        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "recommendations": parsed_output
        })

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid AI JSON"}), 500

    except Exception:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": {
                "message": "AI service temporarily unavailable"
            },
            "is_fallback": True
        }), 200


# -------------------- GENERATE REPORT --------------------

@ai_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()

    error = validate_input(data)
    if error:
        return jsonify({"error": error}), 400

    user_input = data["text"].strip()

    # limit length (ZAP safe)
    if len(user_input) > 500:
        return jsonify({"error": "Input too long"}), 400

    # prompt injection protection
    blocked_words = ["ignore previous", "system prompt", "override", "bypass"]
    if any(word in user_input.lower() for word in blocked_words):
        return jsonify({"error": "Potential prompt injection detected"}), 400

    cached = get_cached(user_input)
    if cached:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": cached,
            "cached": True
        })

    try:
        prompt_template = load_prompt("generate_report.txt")
        final_prompt = prompt_template.replace("{input}", user_input)

        ai_output = generate_response(final_prompt)

        if ai_output is None:
            return jsonify({"error": "AI unavailable"}), 503

        parsed_output = json.loads(ai_output)
        if "is_fallback" in parsed_output:
            return jsonify({
                "generated_at": datetime.utcnow().isoformat(),
                "data": parsed_output["data"],
                "is_fallback": True
            })
        set_cache(user_input, parsed_output)

        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": parsed_output
        })

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid AI JSON"}), 500

    except Exception:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "data": {
                "message": "AI service temporarily unavailable"
            },
            "is_fallback": True
        }), 200
