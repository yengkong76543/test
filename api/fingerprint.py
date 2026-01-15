from flask import Request, jsonify
import os, requests
from datetime import datetime

def handler(request: Request):
    if request.method != "POST":
        return jsonify({"error": "Method not allowed"}), 405

    data = request.get_json(silent=True) or {}

    payload = {
        "ip": request.headers.get("x-forwarded-for", ""),
        "user_agent": request.headers.get("user-agent"),
        "fingerprint": data,
        "created_at": datetime.utcnow().isoformat()
    }

    r = requests.post(
        f"{os.environ['SUPABASE_URL']}/rest/v1/fingerprints",
        headers={
            "apikey": os.environ["SUPABASE_SERVICE_ROLE_KEY"],
            "Authorization": f"Bearer {os.environ['SUPABASE_SERVICE_ROLE_KEY']}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    return jsonify({"ok": True})
