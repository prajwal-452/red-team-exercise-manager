# AI Service — Red Team Exercise Manager

## Overview

This AI service provides intelligent analysis for cybersecurity scenarios.
It generates attack descriptions, recommendations, and detailed reports using an AI model.

---

## Features

* Generate structured attack descriptions
* Provide security recommendations
* Generate detailed incident reports
* Health monitoring with uptime and response time
* Input validation and prompt injection protection
* Fallback handling for AI failures

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/prajwal-452/red-team-exercise-manager.git
cd red-team-exercise-manager/ai-service
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the service

```bash
python app.py
```

Service runs on:

```
http://localhost:5000/health
```

---

## API Endpoints

---

### 🔹 1. POST /describe

**Description:** Generate attack details

**Request:**

```json
{
  "text": "SQL injection attack"
}
```

**Response:**

```json
{
  "generated_at": "...",
  "data": {
    "attack_description": "...",
    "attack_steps": [],
    "impact": "...",
    "risk_level": "High"
  }
}
```

---

### 🔹 2. POST /recommend

**Description:** Get security recommendations

**Response:**

```json
{
  "generated_at": "...",
  "recommendations": [
    {
      "action_type": "Preventive",
      "description": "...",
      "priority": "High"
    }
  ]
}
```

---

### 🔹 3. POST /generate-report

**Description:** Generate full incident report

**Response:**

```json
{
  "generated_at": "...",
  "data": {
    "title": "...",
    "summary": "...",
    "overview": "...",
    "key_items": [],
    "recommendations": []
  }
}
```

---

### 🔹 4. GET /health

**Description:** Service health

```json
{
  "status": "ok",
  "model": "llama-3.1-8b-instant",
  "uptime_seconds": 120,
  "avg_response_time": 0.8
}
```

---

## Security Features

* Input validation
* Prompt injection protection
* Security headers (XSS, CSP, etc.)

---

## Performance

* Average response time under 2 seconds


---

##  Tech Stack

* Python (Flask)
* Groq API (LLM)


---

## Author

AI Developer 1 — Week 1 & Week 2 Implementation
