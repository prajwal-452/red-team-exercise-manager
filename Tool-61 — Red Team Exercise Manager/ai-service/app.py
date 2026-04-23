from flask import Flask
from routes.ai_routes import ai_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(ai_bp)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)