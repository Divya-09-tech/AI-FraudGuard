import re

URGENT_TERMS = [
    "urgent", "immediately", "final warning", "act now",
    "suspended", "blocked", "expires", "today"
]

CREDENTIAL_TERMS = [
    "password", "credentials", "login", "username",
    "bank details", "card details", "verify your identity"
]

MONEY_TERMS = [
    "prize", "cash bonus", "refund", "reward", "gift card",
    "payment", "money"
]

def analyze_signals(sender, subject, body):
    full_text = f"{sender} {subject} {body}".lower()
    signals = []
    points = 0

    urgency_hits = [x for x in URGENT_TERMS if x in full_text]
    if urgency_hits:
        signals.append({
            "type": "Urgency",
            "severity": "medium",
            "detail": f"Pressure language detected: {', '.join(urgency_hits[:3])}"
        })
        points += min(20, 8 + len(urgency_hits) * 3)

    credential_hits = [x for x in CREDENTIAL_TERMS if x in full_text]
    if credential_hits:
        signals.append({
            "type": "Credential request",
            "severity": "high",
            "detail": f"Sensitive-access language detected: {', '.join(credential_hits[:3])}"
        })
        points += min(30, 15 + len(credential_hits) * 4)

    money_hits = [x for x in MONEY_TERMS if x in full_text]
    if money_hits:
        signals.append({
            "type": "Financial lure",
            "severity": "medium",
            "detail": f"Financial/reward language detected: {', '.join(money_hits[:3])}"
        })
        points += min(20, 8 + len(money_hits) * 2)

    urls = re.findall(r"https?://[^\s]+|www\.[^\s]+", full_text)
    if urls:
        suspicious = [
            url for url in urls
            if any(token in url for token in ["paypa1", "verify", "login", "secure", "account"])
        ]
        if suspicious:
            signals.append({
                "type": "Suspicious link",
                "severity": "high",
                "detail": f"Potentially deceptive URL pattern: {suspicious[0][:80]}"
            })
            points += 25
        else:
            signals.append({
                "type": "External link",
                "severity": "low",
                "detail": f"{len(urls)} URL(s) found; reputation is not verified by this demo."
            })
            points += 5

    local_sender = sender.split("@")[-1].lower() if "@" in sender else ""
    if local_sender and any(ch.isdigit() for ch in local_sender):
        signals.append({
            "type": "Sender anomaly",
            "severity": "medium",
            "detail": "Sender domain contains digits; this can be a spoofing signal."
        })
        points += 10

    if "!" in subject:
        signals.append({
            "type": "Subject anomaly",
            "severity": "low",
            "detail": "Attention-seeking punctuation detected."
        })
        points += 3

    return signals, min(points, 70)

def calculate_risk(predicted_label, confidence, rule_points):
    ml_component = {
        "legitimate": 0,
        "spam": 45,
        "phishing": 75
    }.get(predicted_label, 50)

    score = round(min(100, ml_component * 0.55 + rule_points * 0.45), 1)

    if predicted_label == "phishing" and confidence >= 65:
        score = max(score, 75)
    elif predicted_label == "spam" and confidence >= 70:
        score = max(score, 50)

    if score >= 75:
        level, action = "HIGH", "Block / alert security team"
    elif score >= 45:
        level, action = "MEDIUM", "Quarantine for review"
    else:
        level, action = "LOW", "Allow / monitor"

    return score, level, action
