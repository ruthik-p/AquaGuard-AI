"""
model.py
--------
Train, evaluate, save, and load the Random Forest classifier.
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import (
    accuracy_score, f1_score, confusion_matrix, classification_report
)
from sklearn.pipeline import Pipeline
import streamlit as st

from src.preprocessing import build_pipeline, split_features_target
from src.data_loader import FEATURE_COLS

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "rf_model.pkl")


def train_and_save(df: pd.DataFrame, model_path: str = MODEL_PATH) -> dict:
    """
    Train a Random Forest on df, run 5-fold CV + held-out test evaluation,
    persist the pipeline, and return a metrics dict.
    """
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    X, y = split_features_target(df)

    # Held-out test split (stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # Full pipeline: impute → scale → Random Forest
    preprocessing = build_pipeline()
    clf = RandomForestClassifier(
        n_estimators=200,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1,
    )
    pipeline = Pipeline([
        ("preprocessor", preprocessing),
        ("classifier",   clf),
    ])

    # 5-fold cross-validation on training set
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_acc  = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="accuracy")
    cv_f1   = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="f1_macro")

    # Fit on full training set, evaluate on test set
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    metrics = {
        "cv_accuracy_mean":  float(np.mean(cv_acc)),
        "cv_accuracy_std":   float(np.std(cv_acc)),
        "cv_f1_mean":        float(np.mean(cv_f1)),
        "cv_f1_std":         float(np.std(cv_f1)),
        "test_accuracy":     float(accuracy_score(y_test, y_pred)),
        "test_f1_macro":     float(f1_score(y_test, y_pred, average="macro")),
        "confusion_matrix":  confusion_matrix(y_test, y_pred).tolist(),
        "classification_report": classification_report(y_test, y_pred),
        "feature_importances": dict(zip(
            FEATURE_COLS,
            pipeline.named_steps["classifier"].feature_importances_.tolist()
        )),
    }

    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")
    print(f"CV Accuracy: {metrics['cv_accuracy_mean']:.3f} ± {metrics['cv_accuracy_std']:.3f}")
    print(f"Test Accuracy: {metrics['test_accuracy']:.3f}  |  Test F1: {metrics['test_f1_macro']:.3f}")
    return metrics


@st.cache_resource(show_spinner=False)
def load_model(model_path: str = MODEL_PATH) -> Pipeline:
    """Load the persisted pipeline from disk."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Trained model not found at {model_path}. "
            "Run train_and_save() first."
        )
    return joblib.load(model_path)


def predict_single(pipeline: Pipeline, values: dict) -> tuple[float, int]:
    """
    Predict potability for a single sample.
    Returns (probability_of_potable, predicted_class).
    values: dict mapping feature name → float
    """
    X = pd.DataFrame([values])[FEATURE_COLS]
    prob = pipeline.predict_proba(X)[0][1]   # probability of class 1 (potable)
    pred = int(pipeline.predict(X)[0])
    return float(prob), pred


def predict_batch(pipeline: Pipeline, df: pd.DataFrame) -> pd.DataFrame:
    """
    Run predictions on a DataFrame that contains the 9 feature columns.
    Returns df with added columns: risk_probability, predicted_potability.
    """
    X = df[FEATURE_COLS]
    probs = pipeline.predict_proba(X)[:, 1]
    preds = pipeline.predict(X)
    result = df.copy()
    result["risk_probability"] = probs
    result["predicted_potability"] = preds
    return result
