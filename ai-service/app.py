from flask import Flask
from routes.ai_routes import ai_bp
from services.metrics import response_times
from services.ai_service import seed_data
from services.groq_client import GROQ_MODEL
from services.model_loader import MODEL_NAME
import time

app = Flask(__name__)

# Track uptime
start_time = time.time()


# Run startup logic (safe for Docker)
try:
    seed_data()
except:
    pass


# Security headers (ZAP requirement)
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    return response


# Register routes
app.register_blueprint(ai_bp, url_prefix="/ai")


# Health check
@app.route("/health")
def health():
    uptime = time.time() - start_time
    avg_time = sum(response_times) / len(response_times) if response_times else 0

    return {
        "status": "ok",
        "mode": "lightweight-docker",
        "embedding_model": MODEL_NAME,
        "generation_model": GROQ_MODEL,
        "uptime_seconds": round(uptime, 2),
        "avg_response_time": round(avg_time, 2)
    }


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)