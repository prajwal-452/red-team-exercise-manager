from services.model_loader import get_model

# Safe import for chromadb
try:
    import chromadb
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="knowledge_base")
except:
    chromadb = None
    collection = None

# Domain knowledge
DOMAIN_KNOWLEDGE_DOCS = [
    "SQL injection allows attackers to manipulate database queries and can expose or modify sensitive records.",
    "Cross-site scripting (XSS) allows malicious scripts to run in a victim browser and steal session data.",
    "Phishing attacks trick users into revealing credentials, payment data, or internal information.",
    "DDoS attacks overload public services with traffic and can cause business outage or revenue loss.",
    "Ransomware encrypts data and demands payment, often disrupting hospitals, schools, and businesses.",
    "Privilege escalation gives an attacker unauthorized administrative access after an initial compromise.",
    "Secure authentication requires strong password policy, MFA, lockout controls, and session protection.",
    "Input validation and parameterized queries reduce injection risk across APIs, forms, and database calls.",
    "Containerized deployment should avoid hardcoded secrets, run least privilege, and expose only required ports.",
    "Security reports should summarize impact, evidence, risk level, recommendations, and residual risk.",
]


def seed_data():
    model = get_model()

    # If AI not available (Docker case)
    if model is None or collection is None:
        return

    if collection.count() > 0:
        return

    docs = DOMAIN_KNOWLEDGE_DOCS
    embeddings = model.encode(docs).tolist()

    collection.add(
        documents=docs,
        embeddings=embeddings,
        ids=[f"id_{i}" for i in range(len(docs))]
    )


def search_query(text: str):
    model = get_model()

    # Docker fallback (no AI / DB)
    if model is None or collection is None:
        return [
            "AI service running in lightweight mode (no embeddings).",
            "Try running locally for full AI features.",
            "Example: SQL injection is a common web vulnerability."
        ]

    n_results = min(3, collection.count())

    if n_results == 0:
        return []

    query_embedding = model.encode([text]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results["documents"]