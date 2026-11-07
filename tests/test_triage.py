import pytest

from triage import triage


@pytest.mark.parametrize(
    ("text", "category", "priority"),
    [
        ("The client needs an urgent delivery update", "Delivery", "Urgent"),
        ("Vendor payment is overdue", "Billing", "Urgent"),
        ("The shipment is delayed and missing", "Delivery", "High"),
        ("Please prepare the internal report next week", "Internal", "Low"),
    ],
)
def test_triage_sample_data(text, category, priority):
    result = triage(text)

    assert result["category"] == category
    assert result["priority"] == priority


def test_triage_returns_expected_follow_up_fields():
    result = triage("Customer asks for a refund")

    assert set(result) == {
        "category",
        "priority",
        "next_action",
        "draft_follow_up",
    }
    assert result["category"] == "Billing"
    assert "Billing" in result["draft_follow_up"]
    assert "Normal" in result["draft_follow_up"]
