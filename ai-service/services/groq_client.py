from groq import Groq
import os
from dotenv import load_dotenv
import time
from services.metrics import response_times
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response(prompt):
    try:
        start = time.time()

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant"
        )

        end = time.time()
        response_times.append(end - start)

        return response.choices[0].message.content

    except Exception:
        return None