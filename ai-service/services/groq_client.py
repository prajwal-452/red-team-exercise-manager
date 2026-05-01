from groq import Groq
import os
from dotenv import load_dotenv
import time
import json
from services.metrics import response_times
from pathlib import Path
load_dotenv()
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
if not os.getenv("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = "missing_key_fallback_mode"

GROQ_TIMEOUT_SECONDS = float(os.getenv("GROQ_TIMEOUT_SECONDS", "20"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"), timeout=GROQ_TIMEOUT_SECONDS)
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def _fallback_response():
    return json.dumps({
        "is_fallback": True,
        "data": {
            "message": "AI service temporarily unavailable"
        }
    })


def _live_generate_response(prompt):
    start = time.time()

    if not os.getenv("GROQ_API_KEY") or os.getenv("GROQ_API_KEY") == "missing_key_fallback_mode":
        response_times.append(time.time() - start)
        return _fallback_response()

    try:
        result = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=900,
            response_format={"type": "json_object"},
        )

        output = result.choices[0].message.content
        response_times.append(time.time() - start)
        return output
    except Exception:
        response_times.append(time.time() - start)
        return _fallback_response()


def generate_response(prompt):
    return _live_generate_response(prompt)
    raise Exception("test")
    start = time.time()

    try:
        result = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        output = result.choices[0].message.content

        end = time.time()
        response_times.append(end - start)

        return output
    except Exception:
        return json.dumps({
            "is_fallback": True,
            "data": {
                "message": "AI service temporarily unavailable"
            }
        })
