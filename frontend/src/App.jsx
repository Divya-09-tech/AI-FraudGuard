import React, { useState } from "react";
const API = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000/api";

const examples = {
  phishing: {
    sender: "security@paypa1-support.com",
    subject: "Urgent: Verify your account!",
    body: "Your account will be suspended today. Click https://paypa1-login.example.com to verify your password immediately."
  },
  legitimate: {
    sender: "hr@company.com",
    subject: "Interview schedule confirmation",
    body: "Hello, your interview is confirmed for Monday at 11 AM. Please join using the meeting link already shared in the calendar invitation."
  },
  spam: {
    sender: "offers@promo-mail.com",
    subject: "Congratulations! Claim your reward now",
    body: "You have been selected for a special cash bonus. Click now to receive your free gift card."
  }
};

export default function App() {
  const [form, setForm] = useState({ sender: "", subject: "", body: "" });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  function update(key, value) {
    setForm(prev => ({ ...prev, [key]: value }));
  }

  function loadExample(type) {
    setForm(examples[type]);
    setResult(null);
    setError("");
  }

  async function analyze() {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API}/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Analysis failed.");
      setResult(data);
    } catch (e) {
      setError(e.message + " Make sure the Flask backend is running.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <header>
        <div>
          <div className="eyebrow">AI SECURITY PLATFORM</div>
          <h1>AI FraudGuard</h1>
          <p>Explainable email fraud & phishing risk analysis</p>
        </div>
        <div className="badge">ML + Rules + Risk Engine</div>
      </header>

      <main>
        <section className="hero">
          <h2>Analyze a suspicious message</h2>
          <p>Combine NLP classification with transparent security signals to produce an actionable risk decision.</p>

          <div className="examples">
            <button onClick={() => loadExample("phishing")}>Load phishing demo</button>
            <button onClick={() => loadExample("spam")}>Load spam demo</button>
            <button onClick={() => loadExample("legitimate")}>Load legitimate demo</button>
          </div>

          <div className="grid">
            <label>Sender
              <input value={form.sender} onChange={e => update("sender", e.target.value)} placeholder="security@example.com" />
            </label>
            <label>Subject
              <input value={form.subject} onChange={e => update("subject", e.target.value)} placeholder="Email subject" />
            </label>
          </div>

          <label>Message body
            <textarea rows="8" value={form.body} onChange={e => update("body", e.target.value)} placeholder="Paste the email content here..." />
          </label>

          <button className="primary" disabled={loading} onClick={analyze}>
            {loading ? "Analyzing..." : "Analyze with AI"}
          </button>

          {error && <div className="error">{error}</div>}
        </section>

        <section className="result">
          <div className="section-title">
            <span>ANALYSIS RESULT</span>
            {result && <small>{result.model}</small>}
          </div>

          {!result ? (
            <div className="empty">
              <div className="shield">◈</div>
              <h3>Waiting for an email</h3>
              <p>Run one of the demo cases or enter your own message.</p>
            </div>
          ) : (
            <>
              <div className="score-card">
                <div>
                  <div className="label">RISK SCORE</div>
                  <div className="score">{result.risk_score}<span>/100</span></div>
                </div>
                <div className={`risk ${result.risk_level.toLowerCase()}`}>{result.risk_level}</div>
              </div>

              <div className="metrics">
                <div><span>AI prediction</span><strong>{result.prediction.toUpperCase()}</strong></div>
                <div><span>Confidence</span><strong>{result.confidence}%</strong></div>
                <div><span>Action</span><strong>{result.recommended_action}</strong></div>
              </div>

              <h3>Explainable risk signals</h3>
              {result.signals.length === 0 ? (
                <p className="muted">No major rule-based signals were detected.</p>
              ) : (
                <div className="signals">
                  {result.signals.map((s, i) => (
                    <div className="signal" key={i}>
                      <div className={`dot ${s.severity}`}></div>
                      <div><strong>{s.type}</strong><p>{s.detail}</p></div>
                    </div>
                  ))}
                </div>
              )}

              <div className="note">{result.disclaimer}</div>
            </>
          )}
        </section>
      </main>

      <footer>
        <span>AI FraudGuard • Portfolio project</span>
        <span>React • Flask • Scikit-learn • SQLite</span>
      </footer>
    </div>
  );
}
