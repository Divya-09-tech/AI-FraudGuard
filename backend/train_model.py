from pathlib import Path
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "emails.csv"
MODELS = BASE / "models"
MODELS.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        sublinear_tf=True
    )),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ))
])

model.fit(df["text"], df["label"])
joblib.dump(model, MODELS / "fraud_classifier.joblib")

print(f"Trained on {len(df)} examples.")
print(f"Saved model to {MODELS / 'fraud_classifier.joblib'}")
