import os
import requests
from groq import Groq
from dotenv import load_dotenv
import sys

# Load API key
load_dotenv()
if not os.getenv("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = "missing_key_use_endpoint_mode"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
BASE_URL = "http://127.0.0.1:5000"
REQUEST_TIMEOUT_SECONDS = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "60"))

# Load prompt
with open("prompts/describe.txt", "r") as f:
    prompt_template = f.read()


def run_endpoint_dry_run():
    demo_inputs = [
        "Phishing attack on banking users",
        "SQL injection on login page",
        "Ransomware attack on hospital",
        "DDoS attack on ecommerce website",
        "Privilege escalation in internal system",
    ] * 6

    health = requests.get(f"{BASE_URL}/health", timeout=10)
    health.raise_for_status()
    print("HEALTH:", health.json())

    for index, input_text in enumerate(demo_inputs, start=1):
        print(f"\n--- Demo record {index}: {input_text} ---")
        for endpoint in ["/ai/search", "/ai/describe", "/ai/recommend", "/ai/generate-report"]:
            try:
                response = requests.post(
                    f"{BASE_URL}{endpoint}",
                    json={"text": input_text},
                    timeout=REQUEST_TIMEOUT_SECONDS,
                )
                response.raise_for_status()
                print(endpoint, "OK", response.json())
            except requests.exceptions.Timeout:
                print(endpoint, "TIMEOUT", f"no response in {REQUEST_TIMEOUT_SECONDS}s")
            except requests.exceptions.RequestException as error:
                print(endpoint, "ERROR", str(error))

    final_health = requests.get(f"{BASE_URL}/health", timeout=10)
    final_health.raise_for_status()
    print("\nFINAL HEALTH:", final_health.json())


if "--endpoints" in sys.argv:
    run_endpoint_dry_run()
    raise SystemExit(0)

url = "http://127.0.0.1:5000/ai/search"

queries = [
    "security vulnerability",
    "generate report",
    "AI recommendation",
    "docker deployment",
    "red team testing"
] * 6  # 30 queries

for i, q in enumerate(queries):
    res = requests.post(url, json={"text": q})
    print(f"{i+1}: {res.json()}")

# Test inputs
test_inputs = [
    "Phishing attack on banking users",
    "SQL injection on login page",
    "Ransomware attack on hospital",
    "DDoS attack on ecommerce website",
    "Privilege escalation in internal system"
]

for i, input_text in enumerate(test_inputs):
    print(f"\n--- Test {i+1} ---")

    final_prompt = prompt_template.replace("{input}", input_text)
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        model="llama-3.1-8b-instant"
)

    output = response.choices[0].message.content
    print(output)
