from flask import Flask, request, jsonify
import requests, os
from datetime import datetime

app = Flask(__name__)

SUPABASE_URL = os.environ.get["https://zqtpfdecejzfvnbsglgb.supabase.co"]
SUPABASE_KEY = os.environ.get["sb_publishable_71sOetWHfO8f3vy0l6x1dQ_2zv77QKb"]

@app.route("/api/fingerprint", methods=["POST"])
def collect():
    data = request.get_json(silent=True) or {}

    payload = {
        "ip": request.headers.get("x-forwarded-for", request.remote_addr),
        "user_agent": request.headers.get("user-agent"),
        "data": data
    }

    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/fingerprints",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        },
        json=payload,
        timeout=5
    )

    if r.status_code not in (200, 201, 204):
        print("❌ SUPABASE ERROR:", r.text)

    return jsonify({"ok": True})
