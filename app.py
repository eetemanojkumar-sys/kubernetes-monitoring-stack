from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        application="Kubernetes Monitoring Lab",
        status="running"
    )

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/work")
def work():
    # Intentionally performs CPU work for monitoring experiments
    end = time.time() + 0.5

    while time.time() < end:
        sum(i * i for i in range(10000))

    return jsonify(
        status="completed",
        message="CPU work generated"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
