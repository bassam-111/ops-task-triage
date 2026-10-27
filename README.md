# Ops Task Triage

A small, practical automation for operations teams: paste in incoming requests
(client messages, vendor updates, internal tasks) and get them triaged —
category, priority, suggested owner action, and a draft follow-up.

Built to match real operations work: 30+ open tasks a week, multiple accounts,
and follow-ups that must not fall through the cracks.

## What it does

- Classifies a task into: Client, Vendor, Delivery, Billing, or Internal
- Scores priority: Urgent, High, Normal, or Low, from urgency words and deadlines
- Suggests the next action and a short draft follow-up message
- Serves a simple web UI (Flask) and a CSV export of triaged tasks

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Try it (no web UI needed)

```bash
python triage.py "Client asking for urgent delivery update for account A, due today"
```

## Example

Input: "Vendor invoice is overdue and the client is chasing delivery"

Output: Category: Billing · Priority: Urgent · Next action: Chase vendor for
invoice status, then update the client with a revised delivery date.

## Tech

Python, Flask, plain HTML/CSS. No API key required — triage is rule-based,
so it runs offline and is easy to extend with an LLM classifier later.

## Roadmap

- [ ] LLM-based classification option
- [ ] Trello / Google Sheets sync
- [ ] Email ingestion (Gmail)
- [ ] SLA timers and overdue alerts

## Status

Portfolio project by Bassam Zafar (Operations Executive, BS AI — COMSATS
University Islamabad). This README was verified against the local project
files (`triage.py`, `app.py`, `requirements.txt`) in October 2026.
Contributions welcome — please open an issue for bugs or feature ideas.
