"""Rule-based triage for operations tasks.

Category, priority, next action and a draft follow-up, with no external
services required. Extend the keyword maps to fit your own accounts.
"""

import re
import sys

CATEGORIES = {
    "Billing": ["invoice", "payment", "billing", "refund", "quote", "price"],
    "Vendor": ["vendor", "supplier", "delivery partner", "contractor"],
    "Delivery": ["delivery", "shipment", "dispatch", "deadline", "launch", "go-live"],
    "Client": ["client", "customer", "account"],
    "Internal": ["internal", "team", "meeting", "report", "documentation"],
}

URGENT = ["urgent", "asap", "immediately", "overdue", "chasing", "escalat"]
HIGH = ["today", "tomorrow", "blocked", "delay", "missing", "error", "broken"]


def triage(text):
    lower = text.lower()
    category = "Internal"
    for name, keywords in CATEGORIES.items():
        if any(k in lower for k in keywords):
            category = name
            break
    if any(k in lower for k in URGENT):
        priority = "Urgent"
    elif any(k in lower for k in HIGH):
        priority = "High"
    elif "next week" in lower or "when you can" in lower:
        priority = "Low"
    else:
        priority = "Normal"

    actions = {
        "Billing": "Check the invoice/payment status, then update the requester.",
        "Vendor": "Chase the vendor for a status and a firm date, then confirm back.",
        "Delivery": "Confirm the delivery date and blockers, then update the client.",
        "Client": "Acknowledge, confirm the ask, and give a next-update time.",
        "Internal": "Log it, assign an owner, and set a due date.",
    }
    draft = (
        f"Hi, thanks for flagging this. I've logged it as {priority} priority "
        f"({category}) and I'm following up now. I'll update you with the "
        f"next step shortly."
    )
    return {
        "category": category,
        "priority": priority,
        "next_action": actions[category],
        "draft_follow_up": draft,
    }


if __name__ == "__main__":
    task = " ".join(sys.argv[1:]) or "Client asking for a delivery update"
    result = triage(task)
    for key, value in result.items():
        print(f"{key}: {value}")
