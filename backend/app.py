from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Devicely Backend Running 🚀"

@app.route("/api/test", methods=["POST"])
def test_url():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"status": "error", "message": "No URL provided"}), 400

    return jsonify({
        "status": "success",
        "message": "URL received successfully",
        "url": url
    })

if __name__ == "__main__":
    app.run(debug=True)