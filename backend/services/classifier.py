from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "fraud_classifier.joblib"

class EmailClassifier:
    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Model not found. Run `python train_model.py` inside backend first."
            )
        self.model = joblib.load(MODEL_PATH)

    def predict(self, text):
        probabilities = self.model.predict_proba([text])[0]
        classes = list(self.model.classes_)
        ranked = sorted(zip(classes, probabilities), key=lambda item: item[1], reverse=True)
        label, confidence = ranked[0]
        return label, round(float(confidence) * 100, 2)
