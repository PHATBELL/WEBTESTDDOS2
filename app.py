from flask import Flask
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, default_limits=["10 per minute"])

@app.route("/")
def home():
    return "🛡️ Hello Sybau! This is your anti-DDoS test site."

@app.route("/ping")
@limiter.limit("5 per minute")
def ping():
    return "✅ Pong!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
