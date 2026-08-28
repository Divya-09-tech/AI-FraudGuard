# AI FraudGuard — AI-Based Email Fraud & Phishing Risk Management

A portfolio-ready full-stack AI application that analyzes an email/message and estimates whether it is **Legitimate, Spam, or High-Risk Phishing/Fraud**.

## What this demonstrates
- AI/ML classification using TF-IDF + Logistic Regression
- Rule-based risk signals for explainability
- Risk score and recommended action
- REST API with Flask
- React + Vite frontend
- SQLite analysis history
- Model training pipeline
- Input validation and error handling
- Git/GitHub-ready project structure
- Clear architecture suitable for an internship demo

## Architecture
React UI → Flask REST API → Fraud Analysis Service → SQLite

The analysis service combines:
1. TF-IDF + Logistic Regression
2. Explainable security-signal rules
3. A decision engine producing risk score + recommended action

## Run locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python app.py
```

Backend: `http://127.0.0.1:5000`

### Frontend
Open another terminal:
```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL, normally `http://localhost:5173`.

## Demo cases

### High-risk phishing
Sender: `security@paypa1-support.com`

Subject: `Urgent: Verify your account!`

Body:
`Your account will be suspended today. Click https://paypa1-login.example.com to verify your password immediately.`

### Legitimate
Sender: `hr@company.com`

Subject: `Interview schedule confirmation`

Body:
`Hello, your interview is confirmed for Monday at 11 AM. Please join using the meeting link already shared in the calendar invitation.`

### Important portfolio note
This is a demonstration system, not a production anti-fraud service. A real deployment should use a larger representative dataset, proper model evaluation/calibration, SPF/DKIM/DMARC, URL/domain reputation, secure deployment, monitoring, privacy controls and human review.

## Suggested GitHub repository
Name: `ai-fraud-guard`

Description:
> AI-powered email fraud and phishing risk analyzer using NLP, explainable risk signals, Flask REST API, React, and SQLite.
