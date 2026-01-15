import os
import requests
from flask import request, jsonify

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

def handler(req):
    data = req.get_json(silent=True) or {}

    payload = {
        "ip": req.headers.get("x-forwarded-for"),
        "user_agent": req.headers.get("user-agent"),
        "fingerprint": data
    }

    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/fingerprints",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        },
        json=payload
    )

    print("SUPABASE STATUS:", r.status_code)
    print("SUPABASE BODY:", r.text)

    return jsonify({"ok": True})
