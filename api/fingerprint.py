import json
import os
import requests
from datetime import datetime

SUPABASE_URL = os.environ["https://zqtpfdecejzfvnbsglgb.supabase.co"]
SUPABASE_KEY = os.environ["sb_publishable_71sOetWHfO8f3vy0l6x1dQ_2zv77QKb"]

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    try:
        body = request.json() or {}
    except:
        body = {}

    payload = {
        "created_at": datetime.utcnow().isoformat(),
        "ip": request.headers.get("x-forwarded-for", ""),
        "user_agent": request.headers.get("user-agent", ""),
        "fingerprint": body
    }

    res = requests.post(
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

    if res.status_code not in (200, 201, 204):
        return {
            "statusCode": 500,
            "body": res.text
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"ok": True})
    }
