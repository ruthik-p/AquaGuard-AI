# AquaGuard AI

**Intelligent Water Quality Monitoring and Safety Advisory Agent**  
IBM SkillsBuild Machine Learning & Applied AI Internship — Final Project

---

## SDG Alignment

**UN Sustainable Development Goal 6 — Clean Water and Sanitation**  
*Ensure availability and sustainable management of water and sanitation for all.*

---

## Project Overview

AquaGuard AI is a machine-learning-powered web application that analyses nine key water-quality parameters and provides instant risk assessments with plain-English safety guidance. It is built to assist in preliminary screening of water quality and to raise awareness about water safety.

**This tool is for educational and preliminary screening purposes only. It cannot certify that water is safe to drink.**

---

## Features

- 📊 **Dashboard** — Dataset explorer, feature distributions, model performance metrics  
- 🔬 **Predict** — Single-sample prediction with WHO threshold checks and safety advice  
- 📁 **Batch Analysis** — Bulk CSV upload with downloadable risk-assessment report  
- ℹ️ **About** — Methodology, data source, limitations, and disclaimer  

---

## Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.13 |
| Web UI | Streamlit |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn (Random Forest) |
| Visualisation | Plotly |
| Model Persistence | Joblib |

---

## Dataset

**Water Potability Dataset** by Aditya Kadiwal  
Source: [Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability)  
Licence: CC0 1.0 Universal (Public Domain)  
See [`data/DATA_SOURCE.md`](data/DATA_SOURCE.md) for full details.

---

## Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Class balancing:** `class_weight='balanced'`
- **Preprocessing:** Median imputation + Standard scaling
- **Evaluation:** 5-fold stratified cross-validation + held-out 20 % test set
- **Saved model:** `models/rf_model.pkl`

---

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

## Project Structure

```
AquaGuard-AI/
├── app.py                   ← Streamlit home page
├── requirements.txt
├── README.md
├── data/
│   ├── water_potability.csv ← Dataset (CC0)
│   └── DATA_SOURCE.md
├── models/
│   └── rf_model.pkl         ← Trained model
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   └── advisory.py
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Predict.py
│   ├── 3_Batch_Analysis.py
│   └── 4_About.py
├── deliverables/
└── screenshots/
```

---

## Disclaimer

All predictions made by AquaGuard AI are preliminary ML-based screening results only. They cannot certify that water is safe to drink. Always consult a certified laboratory and local health authorities for definitive water-safety assessment.

---

*Built with Python · Streamlit · Scikit-learn · SDG 6*
