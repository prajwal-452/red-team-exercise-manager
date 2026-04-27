from groq import Groq
import os
from dotenv import load_dotenv
import time
import json
from services.metrics import response_times
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response(prompt):
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