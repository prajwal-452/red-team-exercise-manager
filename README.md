# Red Team Exercise Manager – AI Service

## Overview

This project implements an AI-powered service for security testing and red team exercises.
It enables users to analyze vulnerabilities, retrieve relevant knowledge, and generate attack scenarios using AI.

The system is designed with performance, security, and deployability in mind.
It supports both full AI functionality (local environment) and lightweight deployment (Docker).

---

## Tech Stack

* **Backend:** Flask
* **AI Models:** Sentence Transformers (Embeddings)
* **Vector Database:** ChromaDB
* **LLM Integration:** Groq API
* **Containerization:** Docker
* **Security Testing:** OWASP ZAP

---

## Key Features

* Semantic search over security knowledge base
* AI-based vulnerability analysis and recommendations
* REST API endpoints for integration
* Lightweight Docker deployment
* Security hardened with headers and validation
* Fallback mode when AI dependencies are unavailable

---

## Project Structure

```
red-team-exercise-manager/
│
├── ai-service/
│   ├── app.py
│   ├── routes/
│   │   └── ai_routes.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── model_loader.py
│   │   ├── groq_client.py
│   │   └── cache.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── test_prompt.py
│
├── .env.example
├── docker-compose.yml
├── SECURITY.md
└── README.md
```

---

## Setup (Local Environment)

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file:

```
PORT=5000
GROQ_API_KEY=your_actual_api_key
MODEL_NAME=all-MiniLM-L6-v2
```

### 3. Run the application

```
python app.py
```

### 4. Access API

```
http://localhost:5000/health
```

---

## Docker Setup (Lightweight Mode)

### Build image

```
docker build -t ai-service .
```

### Run container

```
docker run -p 5000:5000 ai-service
```

### Notes

* Docker runs in **lightweight mode**
* Heavy AI dependencies are excluded for faster builds
* Fallback responses are returned when AI is unavailable

---

## API Endpoints

### Health Check

**GET /health**

Response:

```
{
  "status": "ok",
  "mode": "lightweight-docker",
  "uptime_seconds": 120,
  "avg_response_time": 80
}
```

---

### AI Search

**POST /ai/search**

Request:

```
{
  "text": "SQL injection"
}
```

Response:

```
{
  "results": [
    "SQL injection allows attackers to manipulate database queries...",
    ...
  ]
}
```

---

## Performance

* Average response time: **50ms – 200ms**
* Model is preloaded in local environment
* Lightweight Docker ensures fast startup

---

## Security

* Security headers implemented:

  * Content Security Policy
  * X-Frame-Options
  * HSTS
* Input validation enforced
* Tested using OWASP ZAP
* No Critical / High vulnerabilities

See `SECURITY.md` for details.

---

## AI Design

### Workflow

1. User input is received via API
2. Input is converted into embeddings
3. ChromaDB retrieves relevant knowledge
4. Groq API generates response
5. Results returned to user

### Fallback Mode

If AI dependencies are unavailable (Docker):

* System returns predefined knowledge responses
* Ensures service availability

---

## Environment Variables

| Variable     | Description      |
| ------------ | ---------------- |
| PORT         | Application port |
| GROQ_API_KEY | API key for Groq |
| MODEL_NAME   | Embedding model  |

---

## Testing

* 30+ prompt tests executed
* Verified consistent responses
* API endpoints validated
* Docker environment tested

---

## Deployment Notes

* Docker used for portability
* Lightweight configuration for faster builds
* Local environment supports full AI functionality

---

## Author

**Prajwal B S**
AI Developer – Red Team Exercise Manager

---

## Status

✔ AI Service Implemented
✔ Dockerized
✔ Security Tested
✔ Ready for Submission
