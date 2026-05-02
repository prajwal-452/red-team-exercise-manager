# AI Service – Red Team Exercise Manager

## Overview

This is the AI microservice built using Flask.
It provides semantic search and AI-based recommendations for security testing.

---

## Setup

### Install dependencies

pip install -r requirements.txt

### Run service

python app.py

---

## Environment Variables

PORT=5000
GROQ_API_KEY=your_api_key_here
MODEL_NAME=all-MiniLM-L6-v2

---

## API Endpoints

### Health

GET /health

### Search

POST /ai/search
Body:
{
"text": "SQL injection"
}

---

## Notes

* Uses embeddings + vector search
* Uses Groq for AI generation
* Lightweight fallback mode in Docker

---
Final submission update

## Author

Prajwal B S
