# 🧠 Tech Fact Bot

A small daily automation: every morning at 10:00 AM PKT, this repo fetches a
tech/programming quote from a free public API and logs it. If the API is
down, it falls back to a curated local list of ~100 tech facts so a day
never goes uncommitted.

- **Primary source:** [Programming Quotes API](https://programming-quotesapi.vercel.app/) (no key required)
- **Fallback:** `backup_facts.json` — curated locally, no external dependency
- **History:** every fact ever shown is appended to `facts_log.json`

## Today's fact

<!-- FACT:START -->
> 💡 **Tech fact** — *(this section updates automatically each morning)*
<!-- FACT:END -->

---
*Part of [shehryar-92](https://github.com/shehryar-92)'s automated GitHub activity setup.*
