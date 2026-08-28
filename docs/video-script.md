# S3K / MYAIGURU self-recorded video script

Target total: approximately 12–14 minutes.

## 1. About yourself and value to S3K — 2–3 minutes

"Hello, I’m Divya Thag, an Electronics and Telecommunication undergraduate with hands-on experience in full-stack software development.

My technical foundation includes JavaScript, React, Node.js, Flask, Python, SQL, data structures and algorithms, object-oriented programming, databases, REST APIs and software development.

For this evaluation, I built an AI-based FraudGuard application from scratch. I wanted to demonstrate not only machine learning, but the complete journey from an AI problem statement to a working product.

The application focuses on email fraud and phishing risk. It uses NLP-based classification together with explainable risk signals and converts those signals into an actionable risk score.

My value to S3K would be at the intersection of AI and software engineering. I can work on the application layer as well as the backend and data layer, and I am interested in building practical AI products rather than treating a model as an isolated notebook.

What interests me about S3K and MYAIGURU is the combination of learning AI, building AI applications and helping organizations adopt AI. I would like to contribute as someone who can learn quickly, build prototypes end-to-end, explain technical decisions clearly, and iterate based on user or client requirements.

I also understand that responsible AI requires attention to false positives, false negatives, data quality, privacy, security, monitoring and human review."

## 2. End-to-end AI application development — 1–2 minutes

"My view is that AI application development should follow the IT SDLC, with AI-specific activities added to each phase.

During ideation, I define the business problem and measurable outcome. During requirements, I identify users, inputs, outputs, constraints, security and success metrics.

During design, I decide the architecture, data flow, model approach, APIs and user experience.

During development, I build the frontend, backend, data pipeline and model integration. AI coding assistants can accelerate boilerplate generation, debugging and documentation, but the developer still owns architecture and validation.

During testing, I test both software behavior and model behavior. For ML, that includes precision, recall, F1, confusion matrix, edge cases and data leakage checks.

During deployment, I package the application, configure secrets, deploy APIs and models, and add logging and monitoring.

During support, I monitor latency, errors, model drift, data quality and user feedback, and continuously improve the model and workflow.

So I see AI tools as a pipeline across the SDLC rather than a single chatbot used only for writing code."

## 3. Demo — 2–3 minutes

Use `docs/demo-script.md`.

## 4. Technical/code walkthrough — 2–3 minutes

"I’ll now show the repository structure.

The backend contains the Flask API, model training script, dataset, classifier service and risk engine.

The model training pipeline uses TF-IDF and Logistic Regression. I selected TF-IDF because it is a strong lightweight baseline for text classification. Logistic Regression is fast and gives class probabilities that are useful for a confidence score.

The risk_engine.py file is important because I wanted explainability. It looks for urgency, credential requests, financial lures, suspicious links and sender anomalies.

The final risk score blends the model classification and rule-based signals. This is a prototype decision layer, not a claim that this formula is production optimal.

The frontend is React. It calls the Flask REST API and presents the decision as a risk score, prediction, confidence, recommended action and explainable signals.

SQLite stores recent analyses. For production, this could be replaced or complemented by PostgreSQL or a cloud database.

I deliberately separated the classifier and risk engine into services so I can replace the ML model, add external reputation APIs, or change decision policy without rewriting the whole application."

## 5. Client-facing sales view — 2 minutes

"I would position FraudGuard as a risk-triage solution rather than simply an email classifier.

The client problem is that employees receive large volumes of suspicious communication, and manually reviewing every message is expensive. An AI layer can prioritize messages that deserve attention.

Target users could include security teams, IT help desks, managed service providers, educational institutions and organizations with high email volumes.

The business value is faster triage, earlier identification of suspicious messages, more consistent decisions, and an auditable explanation of why an email was flagged.

For a client conversation, I would first understand their current workflow and pain points. Then I would propose a pilot using historical or sanitized data, define KPIs such as precision, recall, false-positive rate and analyst time saved, and compare the AI workflow with the existing process.

The product could expand with SPF, DKIM and DMARC checks, domain reputation, URL reputation, attachment analysis, Microsoft 365 or Google Workspace integration, analyst feedback, dashboards and cloud deployment.

The key selling point is not AI for the sake of AI. It is converting unstructured messages into a prioritized, explainable security workflow."

## 6. Internship commitment — 2–3 minutes

Use only statements that are factually true for you:

"I am open to the minimum six-month internship commitment.

I can contribute approximately [YOUR HOURS] hours per week.

My preferred working model is [REMOTE / HYBRID / ONSITE], depending on the internship requirement.

I am comfortable working with cross-functional teams and taking ownership of assigned development tasks.

My strongest areas currently are full-stack development, Python, React, REST APIs, SQL and core computer science fundamentals, and I am actively strengthening my AI/ML and GenAI capabilities.

I would be happy to provide references or additional project information if required.

Thank you for reviewing my application. I would be excited to learn from S3K Technologies and contribute to practical AI solutions."

Do not claim tools, cloud platforms, GenAI, Agentic AI, internships, references, or production experience that you have not actually used.
