# 🧠 Tech Fact Bot

A small daily automation: every morning at 10:00 AM PKT, this repo fetches a
tech/programming quote from a free public API and logs it. If the API is
down, it falls back to a curated local list of ~100 tech facts so a day
never goes uncommitted.

**Live page:** https://shehryar-92.github.io/tech-fact-bot/ — shows today's
fact plus an expandable log of every previous day.

- **Primary source:** [Programming Quotes API](https://programming-quotesapi.vercel.app/) (no key required)
- **Fallback:** `backup_facts.json` — curated locally, no external dependency
- **History:** every fact ever shown is appended to `facts_log.json`, which
  the live page reads directly

## How it works

`fetch_fact.py` runs daily via GitHub Actions (`.github/workflows/daily-fact.yml`).
It tries the API first; on any failure (timeout, bad response, network error)
it falls back to a random unused entry from `backup_facts.json`. Either way,
the result gets appended to `facts_log.json` and committed.

`index.html` is a static page that fetches `facts_log.json` at load time —
no build step, no backend. `404.html` handles any bad routes on GitHub Pages.

---
*Part of [shehryar-92](https://github.com/shehryar-92)'s automated GitHub activity setup.*
