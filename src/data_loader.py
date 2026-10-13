"""
data_loader.py
--------------
Load and cache the water-potability dataset.
"""

import os
import requests
import pandas as pd
import streamlit as st

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "water_potability.csv")

DATASET_URL = (
    "https://raw.githubusercontent.com/nicholasjhana/"
    "water-potability/main/water_potability.csv"
)

FEATURE_COLS = [
    "ph", "Hardness", "Solids", "Chloramines",
    "Sulfate", "Conductivity", "Organic_carbon",
    "Trihalomethanes", "Turbidity",
]
TARGET_COL = "Potability"


def download_dataset(url: str = DATASET_URL, dest: str = DATA_PATH) -> None:
    """Download the dataset CSV if it is not already present."""
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest):
        return
    print(f"Downloading dataset from {url} …")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    with open(dest, "wb") as fh:
        fh.write(response.content)
    print(f"Saved to {dest}")


@st.cache_data(show_spinner=False)
def load_raw_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the CSV and return a raw DataFrame."""
    if not os.path.exists(path):
        download_dataset(dest=path)
    df = pd.read_csv(path)
    return df


def feature_names() -> list[str]:
    return FEATURE_COLS


def target_name() -> str:
    return TARGET_COL
