import json
import os
import requests
from datetime import datetime

def handler(request):
    try:
        data = request.json or {}

        payload = {
            "ip": request.headers.get("x-forwarded-for"),
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

        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
