from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

SUPABASE_URL = "https://zqtpfdecejzfvnbsglgb.supabase.co"
SUPABASE_KEY = "sb_publishable_71sOetWHfO8f3vy0l6x1dQ_2zv77QKb"

@app.route("/", methods=["GET"])
def health():
    return "Flask API is running"

@app.route("/collect", methods=["POST"])
def collect_fingerprint():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/fingerprint",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        },
        json={"data": data}
    )

    return jsonify({"ok": True, "status": r.status_code})
