# Architecture and technical walkthrough

## Input
React collects sender, subject and body and sends JSON to Flask through a REST API.

## NLP classification
**raw text → TF-IDF → Logistic Regression → class + confidence**

TF-IDF converts text into numerical features. Bigrams help capture phrases such as "verify account". Logistic Regression is a lightweight baseline that is fast and provides class probabilities.

## Explainable risk engine
Security indicators include:
- urgency/pressure language
- credential requests
- financial/reward lures
- suspicious URL patterns
- sender-domain anomalies
- attention-seeking punctuation

## Decision engine
The final score blends the ML classification and rule-based signal points:
- 0–44: LOW — Allow / monitor
- 45–74: MEDIUM — Quarantine for review
- 75–100: HIGH — Block / alert security team

## Persistence
SQLite stores recent decisions. A future version can add analyst review, trends, audit logs and dashboards.

## Production evolution
- larger, continuously refreshed dataset
- precision/recall/F1/confusion matrix and calibration
- SPF/DKIM/DMARC
- URL/domain reputation
- attachment analysis
- authentication/RBAC
- Docker + cloud deployment
- monitoring and drift detection
- human-in-the-loop review
- privacy and retention controls
