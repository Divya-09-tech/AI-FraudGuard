# AI FraudGuard — AI-Based Email Fraud & Phishing Risk Management

AI FraudGuard is a full-stack AI/ML application that analyzes email messages and estimates whether they are **Legitimate, Spam, or Phishing/Fraud**.

The system combines machine-learning classification with explainable rule-based security signals to generate a **risk score, risk level, and recommended action**.

## Features

- AI/ML email classification using **TF-IDF + Logistic Regression**
- Explainable rule-based security signals
- Risk score from **0–100**
- Risk levels: **Low, Medium, High**
- Recommended security action
- Detection of suspicious links and credential requests
- Detection of urgency and financial/reward-based language
- Sender and subject anomaly detection
- Flask REST API
- React + Vite frontend
- SQLite analysis history
- Model training pipeline
- Input validation and error handling
- Demo cases for phishing, spam, and legitimate messages

## Technology Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- Flask
- Flask-CORS
- SQLite

### Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Pandas
- NumPy

## System Architecture

```text
┌─────────────────────┐
│    React Frontend   │
│      + Vite         │
└──────────┬──────────┘
           │ HTTP/REST
           ▼
┌─────────────────────┐
│     Flask API       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Fraud Analysis      │
│ Service             │
├─────────────────────┤
│ TF-IDF + Logistic   │
│ Regression          │
│                     │
│ Rule-Based Signals  │
│                     │
│ Risk Engine         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      SQLite         │
│  Analysis History   │
└─────────────────────┘