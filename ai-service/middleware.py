import re

def sanitize_input(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove extra spaces
    text = text.strip()

    return text


def detect_prompt_injection(text):
    suspicious_patterns = [
        "ignore previous instructions",
        "system prompt",
        "act as",
        "bypass",
    ]

    for pattern in suspicious_patterns:
        if pattern in text.lower():
            return True

    return False