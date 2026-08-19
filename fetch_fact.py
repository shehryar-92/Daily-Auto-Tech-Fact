import json
import os
import random
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

API_URL = "https://programming-quotesapi.vercel.app/api/random"
BACKUP_FILE = "backup_facts.json"
LOG_FILE = "facts_log.json"

PKT = timezone(timedelta(hours=5))


def fetch_from_api():
    """Try the live API first. Return None on any failure so we fall back cleanly."""
    try:
        req = urllib.request.Request(API_URL, headers={"User-Agent": "tech-fact-bot"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode())
        quote = (data.get("quote") or data.get("text") or "").strip()
        author = (data.get("author") or "").strip()
        if quote:
            return {"text": quote, "author": author, "source": "api"}
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
            ValueError, KeyError, OSError):
        pass
    return None


def fetch_from_backup():
    """Pick a backup fact, avoiding recent repeats where possible."""
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        facts = json.load(f)

    recent_texts = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            log = json.load(f)
        recent_texts = {entry["text"] for entry in log[-len(facts):]}

    pool = [f for f in facts if f["text"] not in recent_texts] or facts
    fact = random.choice(pool)
    return {"text": fact["text"], "author": fact.get("author", ""), "source": "backup"}


def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_log(log):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


def main():
    result = fetch_from_api() or fetch_from_backup()
    today = datetime.now(PKT).strftime("%Y-%m-%d")

    entry = {
        "date": today,
        "text": result["text"],
        "author": result["author"],
        "source": result["source"],
    }

    log = load_log()
    log.append(entry)
    save_log(log)

    print(f"[{entry['source']}] {entry['text']}" + (f" — {entry['author']}" if entry["author"] else ""))


if __name__ == "__main__":
    main()
