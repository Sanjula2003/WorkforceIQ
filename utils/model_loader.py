import joblib


def load_model():
    return joblib.load(
        "models/attrition_model.pkl"
    )