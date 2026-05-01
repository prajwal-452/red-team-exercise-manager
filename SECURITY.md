# Security Summary

## Executive Summary

The AI service supports red-team exercise descriptions, recommendations, reports, semantic search, health monitoring, caching, fallback handling, and containerized deployment. Current controls focus on input validation, prompt-injection blocking, security headers, secret separation through environment variables, and safe fallback behavior when Groq is unavailable.

## Threats Covered

- Prompt injection attempts such as override, jailbreak, and reveal prompt requests.
- Oversized user input over 500 characters.
- Missing or malformed JSON request bodies.
- AI provider failure or missing API key.
- Browser security header findings commonly reported by ZAP.
- Cache outage, handled without breaking request flow.

## AI Controls

- `sentence-transformers` is loaded during service startup.
- ChromaDB is seeded with 10 security domain knowledge documents.
- Groq generation uses JSON response mode and low temperature for predictable demo output.
- Redis caching is optional and wrapped in fail-safe error handling.
- `/health` reports uptime, average response time, embedding model, and generation model.

## Residual Risks

- A valid Groq API key is required for live AI output.
- Redis is optional locally, but recommended for full cache verification.
- Full ZAP active scan results should be attached after running the scanner on the final deployment.

## Sign-Off

- AI Developer 1: Pending final live endpoint dry run

