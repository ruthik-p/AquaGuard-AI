"""
preprocessing.py
----------------
Imputation and scaling pipeline for the water-potability dataset.
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from src.data_loader import FEATURE_COLS, TARGET_COL


def build_pipeline() -> Pipeline:
    """
    Return a sklearn Pipeline that:
      1. Imputes missing values with the column median.
      2. Scales features with StandardScaler.
    """
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler",  StandardScaler()),
    ])


def split_features_target(df: pd.DataFrame):
    """Return X (feature matrix) and y (target vector)."""
    X = df[FEATURE_COLS].copy()
    y = df[TARGET_COL].copy()
    return X, y


def get_feature_medians(df: pd.DataFrame) -> dict:
    """Return per-feature median values (ignoring NaN) for UI defaults."""
    return {col: float(np.nanmedian(df[col].values)) for col in FEATURE_COLS}
