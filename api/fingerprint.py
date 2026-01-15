import os
import json
import requests

def handler(request):
    try:
        data = request.get_json() or {}
    except Exception:
        data = {}

    payload = {
        "ip": request.headers.get("x-forwarded-for"),
        "user_agent": request.headers.get("user-agent"),
        "fingerprint": data
    }

    r = requests.post(
        f"{os.environ['SUPABASE_URL']}/rest/v1/fingerprints",
        headers={
            "apikey": os.environ['SUPABASE_SERVICE_ROLE_KEY'],
            "Authorization": f"Bearer {os.environ['SUPABASE_SERVICE_ROLE_KEY']}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        },
        json=payload,
        timeout=5
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "ok": True,
            "supabase_status": r.status_code
        })
    }
