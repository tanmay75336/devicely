from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SUPABASE_URL = os.getenv("https://imbdcbabcqgywsekjzaf.supabase.co")
SUPABASE_SERVICE_KEY = os.getenv("sb_publishable_XdsnNg1MkNngbQm4qkbcoA_rdmohZiq")

HEADERS = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "Content-Type": "application/json"
}

# Save Preview
@app.route("/save-preview", methods=["POST"])
def save_preview():
    data = request.json
    user_id = data.get("user_id")
    url = data.get("url")

    if not user_id or not url:
        return jsonify({"error": "Missing data"}), 400

    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/previews",
        headers=HEADERS,
        json={
            "user_id": user_id,
            "url": url
        }
    )

    return jsonify(response.json()), response.status_code


# Get Previews
@app.route("/get-previews/<user_id>")
def get_previews(user_id):
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/previews?user_id=eq.{user_id}&order=created_at.desc",
        headers=HEADERS
    )

    return jsonify(response.json()), response.status_code


if __name__ == "__main__":
    app.run(debug=True)