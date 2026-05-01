# AI Developer 1 Status

## Completed Work

- Preloaded `sentence-transformers` at Flask startup through `load_model()`.
- Seeded ChromaDB with 10 red-team and security domain knowledge documents.
- Enabled `/ai/search`, `/ai/describe`, `/ai/recommend`, `/ai/generate-report`, and `/health` for demo dry runs.
- Removed the runtime effect of the temporary forced Groq failure while preserving the original line for traceability.
- Added Groq JSON response mode, response-time recording, and fallback behavior.
- Added Dockerfile and docker-compose support for the AI service and Redis cache.
- Added exact package versions for the AI runtime dependencies.
- Added `.env.example` values for Groq, Redis, and model configuration.
- Added security headers and stronger prompt-injection checks for AI endpoints.

## Demo Commands

```powershell
cd c:\Users\prajw\Desktop\campuspe\red-team-exercise-manager\ai-service
python -m pip install -r requirements.txt
python app.py
```

In another terminal:

```powershell
cd c:\Users\prajw\Desktop\campuspe\red-team-exercise-manager\ai-service
python test_prompt.py --endpoints
```

Docker test:

```powershell
cd c:\Users\prajw\Desktop\campuspe\red-team-exercise-manager
docker-compose up --build
```

## Demo Inputs

- Phishing attack on banking users
- SQL injection on login page
- Ransomware attack on hospital
- DDoS attack on ecommerce website
- Privilege escalation in internal system

## Health Endpoint

```text
http://127.0.0.1:5000/health
```
