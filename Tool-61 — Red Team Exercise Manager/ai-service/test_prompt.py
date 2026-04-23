import os
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load prompt
with open("prompts/describe.txt", "r") as f:
    prompt_template = f.read()

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