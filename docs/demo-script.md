# 2–3 minute demo script

### 0:00–0:20
"Here is AI FraudGuard, an AI-based email fraud and phishing risk management prototype. The user submits an email and receives a prediction, confidence, risk score, recommended action, and explainable security signals."

### 0:20–1:10
Click **Load phishing demo**, then **Analyze with AI**.

"This example intentionally contains common phishing indicators: urgency, account suspension language, a credential request, and a deceptive-looking domain."

Point to the risk score, HIGH label, prediction/confidence, action, and signals.

"The important design choice is that I don't expose only a binary prediction. I combine the ML output with explainable security signals so an analyst can understand the decision."

### 1:10–1:45
Load the legitimate example and analyze.

"Now I will test a normal HR communication. The same pipeline processes it, but the absence of high-risk signals should produce a substantially lower risk decision."

### 1:45–2:15
"Under the UI, React calls the Flask REST API. Flask passes the text through a TF-IDF plus Logistic Regression classifier, then a rule engine detects security signals. The decision engine combines both into a risk score and recommended action. SQLite stores the analysis for future audit and dashboard functionality."

### 2:15–2:30
"This prototype shows the complete path from user input to AI prediction to an actionable business decision, and the architecture allows additional reputation APIs, authentication signals, models and cloud services to be added later."
