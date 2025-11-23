from flask import Flask, request, jsonify
from recommend import recommend

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"})

@app.route("/recommend", methods=["POST"])
def recommend_api():
    data = request.get_json()
    query = data.get("query")
    top_k = data.get("top_k", 5)
    results = recommend(query, top_k=top_k)
    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000)
