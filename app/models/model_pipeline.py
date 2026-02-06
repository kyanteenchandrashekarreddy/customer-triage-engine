import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import random

# Simple Mock ML Model
class TriageModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = RandomForestClassifier()
        # Mock training data
        data = ["billing issue", "tech support", "reset password", "refund please"]
        labels = ["Billing", "Technical", "Technical", "Billing"]
        X = self.vectorizer.fit_transform(data)
        self.classifier.fit(X, labels)

    def predict(self, text):
        X_vec = self.vectorizer.transform([text])
        category = self.classifier.predict(X_vec)[0]
        priority = "High" if any(word in text.lower() for word in ["urgent", "broken", "refund"]) else "Low"
        return category, priority

# Initialize the model once
model = TriageModel()

def get_prediction(text):
    category, priority = model.predict(text)
    # Mock LLM Summary
    summary = f"Summary: Customer has a {category} inquiry with {priority} priority."
    return {"category": category, "priority": priority, "summary": summary}