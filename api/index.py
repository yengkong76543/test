from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

SUPABASE_URL = os.environ["https://zqtpfdecejzfvnbsglgb.supabase.co"]
SUPABASE_KEY = os.environ["sb_publishable_71sOetWHfO8f3vy0l6x1dQ_2zv77QKb"]

@app.route("/", methods=["POST"])
def collect_fingerprint():
    data = request.get_json()

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
    return jsonify({"ok": True})
