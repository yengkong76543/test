from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Ensure fingerprints directory exists
# Vercel has read-only filesystem, use /tmp
# Other platforms can use current directory
if os.getenv("VERCEL"):
    FINGERPRINT_DIR = "/tmp/fingerprints"
else:
    FINGERPRINT_DIR = os.path.join(os.getcwd(), "fingerprints")

try:
    os.makedirs(FINGERPRINT_DIR, exist_ok=True)
    print(f"✅ Fingerprint directory: {FINGERPRINT_DIR}")
except OSError as e:
    print(f"❌ Failed to create fingerprint directory: {e}")
    # Fallback to /tmp if available
    try:
        FINGERPRINT_DIR = "/tmp/fingerprints"
        os.makedirs(FINGERPRINT_DIR, exist_ok=True)
        print(f"✅ Using /tmp fallback: {FINGERPRINT_DIR}")
    except OSError:
        print("⚠️ Cannot create fingerprint directory - logging disabled")
        FINGERPRINT_DIR = None

# Sample posts data
template_posts = [
    {
        "id": 1,
        "title": "Understanding Civil Law Basics",
        "excerpt": "Key principles of civil law and how they affect daily life.",
        "category": "Civil Law",
        "author": "Jane Doe",
        "date": "2025-01-10",
    },
    {
        "id": 2,
        "title": "Intellectual Property Rights in the Digital Age",
        "excerpt": "Protecting your creations online: copyrights, trademarks, and patents.",
        "category": "IP Law",
        "author": "John Smith",
        "date": "2025-01-08",
    },
    {
        "id": 3,
        "title": "Employment Law: What Employees Should Know",
        "excerpt": "Contracts, overtime, and workplace rights summarized.",
        "category": "Employment Law",
        "author": "Emma Lee",
        "date": "2025-01-05",
    },
]


@app.route("/")
def index():
    return render_template("index.html", posts=template_posts)


@app.route("/api/fingerprint", methods=["POST"])
def api_fingerprint():
    """Log browser fingerprints"""
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return jsonify({"status": "ok"}), 200
        
        data["server_timestamp"] = datetime.utcnow().isoformat() + "Z"
        data["ip_address"] = request.headers.get("X-Forwarded-For", request.remote_addr) or request.remote_addr
        data["request_headers"] = {
            "user-agent": request.headers.get("User-Agent"),
            "accept-language": request.headers.get("Accept-Language"),
            "accept-encoding": request.headers.get("Accept-Encoding"),
            "accept": request.headers.get("Accept"),
        }

        # Only save if directory is available
        if FINGERPRINT_DIR:
            # Save individual file
            timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%f")
            fname = f"fingerprint_{timestamp}.json"
            fpath = os.path.join(FINGERPRINT_DIR, fname)
            try:
                with open(fpath, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"✅ Saved: {fname}")
            except (IOError, OSError) as e:
                print(f"⚠️ Save failed: {e}")

            # Append to log file
            log_path = os.path.join(FINGERPRINT_DIR, "fingerprints_log.jsonl")
            try:
                with open(log_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(data, ensure_ascii=False) + "\n")
                print(f"✅ Logged fingerprint from {data.get('ip_address', 'unknown')}")
            except (IOError, OSError) as e:
                print(f"⚠️ Log failed: {e}")
        else:
            # Just print to console if no directory available
            print(f"📊 Fingerprint received from {data.get('ip_address', 'unknown')}: {data.get('userAgent', 'unknown')[:50]}")

        return jsonify({"status": "ok"}), 200
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"⚠️ Fingerprint error: {e}")
        return jsonify({"status": "ok"}), 200
