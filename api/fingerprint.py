import json
import os
import requests
from datetime import datetime

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Method not allowed"})
        }

    try:
        data = request.json() or {}
    except Exception:
        data = {}

    payload = {
        "ip": request.headers.get("x-forwarded-for", request.headers.get("x-real-ip")),
        "user_agent": request.headers.get("user-agent"),
        "fingerprint": data,
        "created_at": datetime.utcnow().isoformat()
    }

    r = requests.post(
        f"{os.environ['SUPABASE_URL']}/rest/v1/fingerprints",
        headers={
            "apikey": os.environ["SUPABASE_SERVICE_ROLE_KEY"],
            "Authorization": f"Bearer {os.environ['SUPABASE_SERVICE_ROLE_KEY']}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        },
        json=payload,
        timeout=5
    )

    # 🔥 LOG SUPABASE RESPONSE (CỰC QUAN TRỌNG)
    if r.status_code not in (200, 201, 204):
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "error": "Supabase insert failed",
                "status": r.status_code,
                "detail": r.text
            })
        }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"ok": True})
    }
