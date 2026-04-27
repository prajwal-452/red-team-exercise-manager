from flask import Flask
from routes.ai_routes import ai_bp
from services.metrics import response_times
import time

start_time = time.time()

app = Flask(__name__)
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

# Register routes
app.register_blueprint(ai_bp)

@app.route("/health")
def health():
    uptime = time.time() - start_time

    avg_time = sum(response_times) / len(response_times) if response_times else 0

    return {
        "status": "ok",
        "model": "llama-3.1-8b-instant",
        "uptime_seconds": round(uptime, 2),
        "avg_response_time": round(avg_time, 2)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

