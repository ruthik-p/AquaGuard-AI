"""
pages/4_About.py
----------------
Premium About page: SDG context, methodology, data source, limitations, disclaimer.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from src.styles import get_global_css, disclaimer_bar, divider

st.set_page_config(
    page_title="About — AquaGuard AI",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(get_global_css(), unsafe_allow_html=True)

# ── Sidebar brand ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding:1rem 0 1.5rem 0;">
            <div style="font-size:2rem;">💧</div>
            <div style="font-weight:700; color:#00d4ff; font-size:1rem;">AquaGuard AI</div>
        </div>
        <hr style="border-color:#1a3a5c;">
        """,
        unsafe_allow_html=True,
    )

# ── Page header ────────────────────────────────────────────────────────────────
st.markdown(disclaimer_bar(), unsafe_allow_html=True)

st.markdown(
    """
    <div class="aq-animate-up">
        <h1 style="font-size:2rem; font-weight:800; color:#e8f4fd; margin-bottom:0.25rem;">
            About AquaGuard AI
        </h1>
        <p style="color:#8bafc7; margin-top:0; font-size:0.95rem;">
            Project context, methodology, dataset information, and important limitations.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(divider(), unsafe_allow_html=True)

# ── SDG 6 section ──────────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">UN Sustainable Development Goal 6</h2>',
    unsafe_allow_html=True,
)

sdg_col, stat_col = st.columns([2, 1])

with sdg_col:
    st.markdown(
        """
        <div class="aq-card">
            <p style="color:#e8f4fd; font-size:1rem; line-height:1.8; margin:0;">
                <strong style="color:#00d4ff;">SDG 6 — Clean Water and Sanitation</strong> calls
                for ensuring the availability and sustainable management of water and sanitation
                for all by 2030.
            </p>
            <p style="color:#8bafc7; font-size:0.9rem; line-height:1.8; margin:0.75rem 0 0 0;">
                Access to safe drinking water is a fundamental human right. Contaminated water
                causes preventable diseases including cholera, dysentery, typhoid, and polio.
                AquaGuard AI is a proof-of-concept tool that demonstrates how machine learning
                can assist in preliminary water-quality screening — helping communities, field
                workers, and researchers flag samples that require further professional testing.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stat_col:
    st.markdown(
        """
        <div class="aq-card" style="text-align:center;">
            <p style="font-size:2.5rem; font-weight:800; color:#ff4d6d; margin:0; line-height:1.1;">2B+</p>
            <p style="color:#8bafc7; font-size:0.8rem; margin:0.3rem 0 1rem 0;">People lack safe water</p>
            <p style="font-size:2rem; font-weight:800; color:#ffb347; margin:0; line-height:1.1;">80%</p>
            <p style="color:#8bafc7; font-size:0.8rem; margin:0.3rem 0 1rem 0;">Wastewater untreated</p>
            <p style="font-size:2rem; font-weight:800; color:#00c896; margin:0; line-height:1.1;">SDG 6</p>
            <p style="color:#8bafc7; font-size:0.8rem; margin:0.3rem 0 0 0;">UN 2030 target</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="color:#3a5a76; font-size:0.68rem; text-align:center; margin-top:0.3rem;">'
        'Source: UN Water / WHO, 2022</p>',
        unsafe_allow_html=True,
    )

st.markdown(divider(), unsafe_allow_html=True)

# ── Dataset section ────────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Dataset</h2>',
    unsafe_allow_html=True,
)

ds_col1, ds_col2 = st.columns(2)

with ds_col1:
    st.markdown(
        """
        <div class="aq-card">
            <p style="color:#8bafc7; font-size:0.78rem; text-transform:uppercase;
                      letter-spacing:0.06em; font-weight:600; margin:0 0 0.75rem 0;">Dataset Information</p>
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; color:#e8f4fd;">
                <tr><td style="padding:0.4rem 0; color:#8bafc7; width:40%;">Name</td>
                    <td>Water Quality and Potability</td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Author</td>
                    <td>Aditya Kadiwal</td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Source</td>
                    <td><a href="https://www.kaggle.com/datasets/adityakadiwal/water-potability"
                           style="color:#00d4ff;" target="_blank">Kaggle</a></td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Licence</td>
                    <td><span class="aq-badge aq-badge-green">CC0 1.0 Public Domain</span></td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Rows</td>
                    <td>3,276 water samples</td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Target</td>
                    <td>Potability: 1 = Potable, 0 = Not Potable</td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Missing Values</td>
                    <td>ph (491), Sulfate (781), Trihalomethanes (162)</td></tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )

with ds_col2:
    st.markdown(
        """
        <div class="aq-card">
            <p style="color:#8bafc7; font-size:0.78rem; text-transform:uppercase;
                      letter-spacing:0.06em; font-weight:600; margin:0 0 0.75rem 0;">Nine Features</p>
        """,
        unsafe_allow_html=True,
    )
    features_data = [
        ("ph",               "6.5 – 8.5",    "pH value"),
        ("Hardness",         "< 300 mg/L",    "Calcium / magnesium salts"),
        ("Solids",           "< 500 ppm",     "Total dissolved solids (TDS)"),
        ("Chloramines",      "< 4 ppm",       "Disinfectant residuals"),
        ("Sulfate",          "< 250 mg/L",    "Dissolved sulfates"),
        ("Conductivity",     "< 400 μS/cm",   "Ionic concentration"),
        ("Organic_carbon",   "< 2 ppm",       "Organic compound load"),
        ("Trihalomethanes",  "< 80 μg/L",     "Chlorination by-products"),
        ("Turbidity",        "< 5 NTU",       "Particle cloudiness"),
    ]
    rows_html = ""
    for feat, limit, desc in features_data:
        rows_html += (
            f'<tr><td style="padding:0.3rem 0; color:#00d4ff; font-size:0.82rem;">{feat}</td>'
            f'<td style="padding:0.3rem 0.5rem; color:#8bafc7; font-size:0.82rem;">{desc}</td>'
            f'<td style="padding:0.3rem 0; text-align:right;">'
            f'<span class="aq-badge aq-badge-cyan" style="font-size:0.68rem;">{limit}</span></td></tr>'
        )
    st.markdown(
        f'<table style="width:100%; border-collapse:collapse;">{rows_html}</table></div>',
        unsafe_allow_html=True,
    )

st.markdown(divider(), unsafe_allow_html=True)

# ── Methodology section ────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">ML Methodology</h2>',
    unsafe_allow_html=True,
)

meth_col1, meth_col2 = st.columns(2)

with meth_col1:
    st.markdown(
        """
        <div class="aq-card" style="height:100%;">
            <p style="color:#00d4ff; font-size:0.85rem; font-weight:700; text-transform:uppercase;
                      letter-spacing:0.06em; margin:0 0 0.75rem 0;">Preprocessing</p>
            <ol style="color:#8bafc7; font-size:0.88rem; line-height:1.9; margin:0; padding-left:1.2rem;">
                <li><strong style="color:#e8f4fd;">Median imputation</strong> — replaces missing values
                    (ph, Sulfate, THMs) with per-feature medians. Robust to outliers.</li>
                <li><strong style="color:#e8f4fd;">StandardScaler</strong> — normalises all features
                    to zero mean / unit variance. Best practice for ensemble pipelines.</li>
                <li><strong style="color:#e8f4fd;">No feature engineering</strong> — nine raw
                    measurements are used directly for transparency and reproducibility.</li>
            </ol>
            <p style="color:#00d4ff; font-size:0.85rem; font-weight:700; text-transform:uppercase;
                      letter-spacing:0.06em; margin:1rem 0 0.75rem 0;">Model</p>
            <ul style="color:#8bafc7; font-size:0.88rem; line-height:1.9; margin:0; padding-left:1.2rem;">
                <li><strong style="color:#e8f4fd;">Random Forest Classifier</strong> (scikit-learn)</li>
                <li>200 trees · <code style="color:#00d4ff;">class_weight='balanced'</code></li>
                <li>Handles class imbalance (~61% not-potable / 39% potable)</li>
                <li>Native feature importances for interpretability</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with meth_col2:
    st.markdown(
        """
        <div class="aq-card" style="height:100%;">
            <p style="color:#00d4ff; font-size:0.85rem; font-weight:700; text-transform:uppercase;
                      letter-spacing:0.06em; margin:0 0 0.75rem 0;">Evaluation</p>
            <ul style="color:#8bafc7; font-size:0.88rem; line-height:1.9; margin:0; padding-left:1.2rem;">
                <li>80/20 stratified train/test split</li>
                <li>5-fold stratified cross-validation on training set</li>
                <li>Metrics: Accuracy, F1-macro, Confusion Matrix</li>
                <li>All metrics computed on unseen data — no data leakage</li>
            </ul>
            <p style="color:#00d4ff; font-size:0.85rem; font-weight:700; text-transform:uppercase;
                      letter-spacing:0.06em; margin:1rem 0 0.75rem 0;">Actual Model Performance</p>
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem;">
                <tr>
                    <td style="padding:0.35rem 0; color:#8bafc7;">CV Accuracy (5-fold)</td>
                    <td style="text-align:right;">
                        <span class="aq-badge aq-badge-cyan">0.669 ± 0.016</span>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0.35rem 0; color:#8bafc7;">CV F1 Macro</td>
                    <td style="text-align:right;">
                        <span class="aq-badge aq-badge-cyan">0.640 ± 0.019</span>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0.35rem 0; color:#8bafc7;">Test Accuracy</td>
                    <td style="text-align:right;">
                        <span class="aq-badge aq-badge-cyan">0.642</span>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0.35rem 0; color:#8bafc7;">Test F1 Macro</td>
                    <td style="text-align:right;">
                        <span class="aq-badge aq-badge-cyan">0.602</span>
                    </td>
                </tr>
            </table>
            <p style="color:#3a5a76; font-size:0.72rem; margin:0.75rem 0 0 0;">
                The ~64% accuracy reflects the genuine difficulty of this dataset —
                feature distributions overlap significantly between classes. Metrics
                are not inflated or cherry-picked.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Pipeline diagram ────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    '<p style="color:#8bafc7; font-size:0.85rem; font-weight:600; '
    'text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;">Pipeline Architecture</p>',
    unsafe_allow_html=True,
)
st.code(
    """Raw CSV
  └─► SimpleImputer (median)
        └─► StandardScaler
              └─► RandomForestClassifier(n_estimators=200, class_weight='balanced')
                    ├─► 5-fold StratifiedKFold → CV Accuracy & F1 (reported)
                    └─► Held-out 20% Test Set  → Test Accuracy & F1 (reported)
                          └─► joblib.dump → models/rf_model.pkl""",
    language="text",
)

st.markdown(divider(), unsafe_allow_html=True)

# ── Advisory logic ─────────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Advisory Logic</h2>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="aq-card">
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1.5rem;">
            <div>
                <p style="color:#00d4ff; font-weight:700; font-size:0.88rem;
                          text-transform:uppercase; letter-spacing:0.05em; margin:0 0 0.5rem 0;">
                    Risk Tiers</p>
                <div class="aq-violation" style="margin-bottom:0.4rem;">
                    <span class="aq-violation-title">High Risk</span>
                    <span style="color:#8bafc7; font-size:0.8rem;"> — Potability prob &lt; 35%</span>
                </div>
                <div style="background:rgba(255,179,71,0.07); border-left:3px solid #ffb347;
                            border-radius:0 8px 8px 0; padding:0.5rem 0.75rem; margin-bottom:0.4rem;">
                    <span style="color:#ffb347; font-weight:600; font-size:0.85rem;">Moderate Risk</span>
                    <span style="color:#8bafc7; font-size:0.8rem;"> — 35–65%</span>
                </div>
                <div style="background:rgba(0,200,150,0.07); border-left:3px solid #00c896;
                            border-radius:0 8px 8px 0; padding:0.5rem 0.75rem;">
                    <span style="color:#00c896; font-weight:600; font-size:0.85rem;">Low Risk</span>
                    <span style="color:#8bafc7; font-size:0.8rem;"> — prob ≥ 65%</span>
                </div>
            </div>
            <div>
                <p style="color:#00d4ff; font-weight:700; font-size:0.88rem;
                          text-transform:uppercase; letter-spacing:0.05em; margin:0 0 0.5rem 0;">
                    WHO Checks</p>
                <p style="color:#8bafc7; font-size:0.85rem; line-height:1.7; margin:0;">
                    Each of the 9 parameters is independently compared against documented
                    WHO / standard guideline thresholds. Violations trigger specific
                    plain-English explanations and targeted next-step guidance.
                </p>
            </div>
            <div>
                <p style="color:#00d4ff; font-weight:700; font-size:0.88rem;
                          text-transform:uppercase; letter-spacing:0.05em; margin:0 0 0.5rem 0;">
                    Guidance Logic</p>
                <p style="color:#8bafc7; font-size:0.85rem; line-height:1.7; margin:0;">
                    Next steps are generated from risk tier + specific violations. Turbidity
                    violations trigger filtration advice; THM violations trigger aeration advice;
                    pH violations trigger neutralisation advice.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(divider(), unsafe_allow_html=True)

# ── Limitations ────────────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Known Limitations</h2>',
    unsafe_allow_html=True,
)

limitations = [
    (
        "Educational Dataset",
        "The water-potability dataset is widely used for ML education but is not derived "
        "from a verified real-world monitoring programme. It should not be used to make "
        "real drinking-water decisions.",
    ),
    (
        "Binary Classification Only",
        "The model predicts 'potable' or 'not potable' at a single probability threshold. "
        "It cannot quantify specific contaminant concentrations or identify the type of contamination.",
    ),
    (
        "Missing Value Imputation",
        "Samples with missing measurements use the dataset median — this introduces "
        "uncertainty. Real measurements are always preferable.",
    ),
    (
        "No Spatial or Temporal Context",
        "The model does not account for geographic location, seasonal variation, or "
        "historical trends in water quality.",
    ),
    (
        "Class Imbalance",
        "Even with balanced class weights, the model may have different precision/recall "
        "trade-offs across classes (~79% recall for not-potable vs ~42% for potable). "
        "Review the confusion matrix on the Dashboard.",
    ),
    (
        "Not a Regulatory Tool",
        "This application is not certified by any health or environmental authority and "
        "must not be used as the sole basis for drinking-water safety decisions.",
    ),
]

lim_cols = st.columns(2)
for i, (title, text) in enumerate(limitations):
    with lim_cols[i % 2]:
        st.markdown(
            f"""
            <div class="aq-card" style="padding:1rem 1.25rem; margin-bottom:0.75rem;">
                <p style="color:#ffb347; font-weight:600; font-size:0.88rem; margin:0 0 0.4rem 0;">
                    {i+1}. {title}
                </p>
                <p style="color:#8bafc7; font-size:0.84rem; line-height:1.7; margin:0;">{text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(divider(), unsafe_allow_html=True)

# ── Disclaimer ──────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="aq-risk-high" style="padding:1.5rem 2rem;">
        <p style="color:#ff4d6d; font-size:1.1rem; font-weight:800; margin:0 0 0.75rem 0;">
            Important Disclaimer
        </p>
        <p style="color:#e8f4fd; font-size:0.9rem; line-height:1.8; margin:0 0 0.5rem 0;">
            All predictions and assessments produced by AquaGuard AI are
            <strong>preliminary machine-learning-based screening results only</strong>.
        </p>
        <p style="color:#8bafc7; font-size:0.88rem; line-height:1.8; margin:0 0 0.5rem 0;">
            They <strong style="color:#ff4d6d;">cannot certify</strong> that water is safe or
            unsafe to drink. The model has real-world accuracy limitations (~64% test accuracy)
            and may produce false positives or false negatives.
        </p>
        <p style="color:#8bafc7; font-size:0.88rem; line-height:1.8; margin:0;">
            <strong style="color:#e8f4fd;">Always consult a certified laboratory and local health
            authorities</strong> for definitive water-safety assessment before making any
            decisions about water consumption.
        </p>
        <p style="color:#5a7a96; font-size:0.78rem; margin:0.75rem 0 0 0;">
            AquaGuard AI is developed as an educational project for the IBM SkillsBuild
            Machine Learning &amp; Applied AI Internship. It is not intended for operational
            or regulatory use.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(divider(), unsafe_allow_html=True)

# ── Project info ────────────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Project Information</h2>',
    unsafe_allow_html=True,
)

proj_col1, proj_col2 = st.columns(2)
with proj_col1:
    st.markdown(
        """
        <div class="aq-card">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem;">
                <tr><td style="padding:0.4rem 0; color:#8bafc7; width:45%;">Project Title</td>
                    <td style="color:#e8f4fd;">AquaGuard AI</td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Full Title</td>
                    <td style="color:#e8f4fd;">Intelligent Water Quality Monitoring &amp; Safety Advisory Agent</td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Programme</td>
                    <td style="color:#e8f4fd;">IBM SkillsBuild ML &amp; Applied AI Internship</td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">SDG Alignment</td>
                    <td><span class="aq-badge aq-badge-cyan">SDG 6 — Clean Water &amp; Sanitation</span></td></tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
with proj_col2:
    st.markdown(
        """
        <div class="aq-card">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem;">
                <tr><td style="padding:0.4rem 0; color:#8bafc7; width:45%;">Language</td>
                    <td><span class="aq-badge aq-badge-cyan">Python 3.13</span></td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Web Framework</td>
                    <td><span class="aq-badge aq-badge-cyan">Streamlit 1.65</span></td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">ML Library</td>
                    <td><span class="aq-badge aq-badge-cyan">Scikit-learn 1.9</span></td></tr>
                <tr><td style="padding:0.4rem 0; color:#8bafc7;">Dataset Licence</td>
                    <td><span class="aq-badge aq-badge-green">CC0 Public Domain</span></td></tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="aq-footer">
        AquaGuard AI · About · IBM SkillsBuild ML &amp; Applied AI Internship · SDG 6
    </div>
    """,
    unsafe_allow_html=True,
)
