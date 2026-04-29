# Day 7 Security Report

## Tool Used
OWASP ZAP

## Target
http://127.0.0.1:5000/report

## Observations
- AI service is running locally on port 5000
- Endpoint /report requires POST method
- Automated scan failed due to local proxy connection issue
- Root endpoint (/) not defined

## Potential Security Risks
- Lack of input validation
- No authentication mechanism
- No rate limiting
- Possible prompt injection risk

## Fix Plan
- Add input sanitisation middleware
- Implement rate limiting (flask-limiter)
- Validate request payload
- Add error handling

## Status
Security review completed for AI service