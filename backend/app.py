from pathlib import Path
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

from services.classifier import EmailClassifier
from services.risk_engine import analyze_signals, calculate_risk

app = Flask(__name__)
CORS(app)

BASE = Path(__file__).resolve().parent
DB_PATH = BASE / "fraud_guard.db"

classifier = EmailClassifier()

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT,
                subject TEXT,
                label TEXT,
                confidence REAL,
                risk_score REAL,
                risk_level TEXT,
                action TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

init_db()

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "AI FraudGuard"})

@app.post("/api/analyze")
def analyze():
    data = request.get_json(silent=True) or {}

    sender = str(data.get("sender", "")).strip()
    subject = str(data.get("subject", "")).strip()
    body = str(data.get("body", "")).strip()

    if not body:
        return jsonify({"error": "Email body is required."}), 400

    if len(body) > 10000:
        return jsonify({"error": "Email body is too long for this demo."}), 400

    combined = f"Subject: {subject}\nFrom: {sender}\n{body}"
    label, confidence = classifier.predict(combined)
    signals, rule_points = analyze_signals(sender, subject, body)
    risk_score, risk_level, action = calculate_risk(label, confidence, rule_points)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO analyses
            (sender, subject, label, confidence, risk_score, risk_level, action)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (sender, subject, label, confidence, risk_score, risk_level, action))
        conn.commit()

    return jsonify({
        "prediction": label,
        "confidence": confidence,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "recommended_action": action,
        "signals": signals,
        "model": "TF-IDF + Logistic Regression",
        "disclaimer": "Demo classifier; not a production security verdict."
    })

@app.get("/api/history")
def history():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT id, sender, subject, label, confidence,
                   risk_score, risk_level, action, created_at
            FROM analyses
            ORDER BY id DESC
            LIMIT 10
        """).fetchall()
    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
