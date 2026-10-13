"""
app.py — AquaGuard AI
Premium landing page for the Streamlit multi-page application.
"""

import os
import sys
import streamlit as st

sys.path.insert(0, os.path.dirname(__file__))

from src.styles import get_global_css, footer, disclaimer_bar, divider

st.set_page_config(
    page_title="AquaGuard AI — Water Quality Intelligence",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(get_global_css(), unsafe_allow_html=True)

# ── Sidebar brand ──────────────────────────────────────────────────────────────

# ── Sidebar brand and navigation ───────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding: 1rem 0 1.5rem 0;">
            <div style="font-size:2.2rem; margin-bottom:0.3rem;">💧</div>
            <div style="font-size:1.1rem; font-weight:700; color:#00d4ff;">AquaGuard AI</div>
            <div style="font-size:0.72rem; color:#5a7a96; margin-top:0.25rem;">
                Water Quality Intelligence
            </div>
        </div>
        <hr style="border-color:#1a3a5c; margin-bottom:1rem;">
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🧭 Navigation")

    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/1_Dashboard.py", label="Dashboard", icon="📊")
    st.page_link("pages/2_Predict.py", label="Water Quality Predictor", icon="🔬")
    st.page_link("pages/3_Batch_Analysis.py", label="Batch Analysis", icon="📁")
    st.page_link("pages/4_About.py", label="About Project", icon="ℹ️")

    st.markdown("---")
    st.markdown(
        """
        <div style="font-size:0.72rem; color:#3a5a76; line-height:1.6;">
            IBM SkillsBuild ML &amp; Applied AI Internship<br>
            Final Project · SDG 6
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Disclaimer ─────────────────────────────────────────────────────────────────
st.markdown(disclaimer_bar(), unsafe_allow_html=True)

# ── Hero section ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="aq-hero aq-animate-up">
        <div style="margin-bottom:1rem;">
            <span class="aq-badge aq-badge-cyan">SDG 6 — Clean Water &amp; Sanitation</span>
            &nbsp;
            <span class="aq-badge aq-badge-green">IBM SkillsBuild · Final Project</span>
        </div>
        <h1 class="aq-hero-title">Intelligent Water Quality<br>Monitoring &amp; Safety AI</h1>
        <p class="aq-hero-subtitle">AquaGuard AI</p>
        <p class="aq-hero-desc">
            Machine-learning-powered analysis of nine critical water-quality parameters.
            Instant risk assessment, WHO guideline checks, and plain-English safety guidance —
            supporting communities, researchers, and field workers worldwide.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Hero SVG illustration ──────────────────────────────────────────────────────
col_hero_l, col_hero_c, col_hero_r = st.columns([1, 2, 1])
with col_hero_c:
    st.markdown(
        """
        <div style="text-align:center; padding: 0.5rem 0 1.5rem 0;">
        <svg viewBox="0 0 480 200" xmlns="http://www.w3.org/2000/svg"
             style="width:100%; max-width:480px; height:auto;">
          <defs>
            <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%"   stop-color="#00d4ff" stop-opacity="0.6"/>
              <stop offset="50%"  stop-color="#0099cc" stop-opacity="0.8"/>
              <stop offset="100%" stop-color="#00c896" stop-opacity="0.6"/>
            </linearGradient>
            <linearGradient id="waveGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%"   stop-color="#0099cc" stop-opacity="0.3"/>
              <stop offset="100%" stop-color="#00d4ff" stop-opacity="0.5"/>
            </linearGradient>
            <linearGradient id="dropGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%"   stop-color="#00d4ff"/>
              <stop offset="100%" stop-color="#0066aa"/>
            </linearGradient>
          </defs>
          <!-- Background glow circles -->
          <circle cx="240" cy="100" r="90" fill="rgba(0,212,255,0.03)"/>
          <circle cx="240" cy="100" r="60" fill="rgba(0,212,255,0.04)"/>
          <!-- Wave 1 (back) -->
          <path d="M0,130 C60,110 120,150 180,130 C240,110 300,150 360,130 C420,110 460,140 480,130 L480,200 L0,200 Z"
                fill="url(#waveGrad2)"/>
          <!-- Wave 2 (front) -->
          <path d="M0,150 C80,130 160,170 240,150 C320,130 400,170 480,150 L480,200 L0,200 Z"
                fill="url(#waveGrad)"/>
          <!-- Water drop icon -->
          <g transform="translate(215, 20)">
            <path d="M25,0 C25,0 0,35 0,50 C0,63.8 11.2,75 25,75 C38.8,75 50,63.8 50,50 C50,35 25,0 25,0 Z"
                  fill="url(#dropGrad)" opacity="0.9"/>
            <path d="M25,15 C25,15 10,42 10,52 C10,59.7 16.8,66 25,66 C33.2,66 40,59.7 40,52 C40,42 25,15 25,15 Z"
                  fill="rgba(255,255,255,0.25)"/>
          </g>
          <!-- Scanning lines -->
          <line x1="60" y1="60" x2="160" y2="60" stroke="#00d4ff" stroke-width="0.8" stroke-opacity="0.3" stroke-dasharray="4,4"/>
          <line x1="320" y1="60" x2="420" y2="60" stroke="#00d4ff" stroke-width="0.8" stroke-opacity="0.3" stroke-dasharray="4,4"/>
          <line x1="30" y1="90" x2="130" y2="90" stroke="#00c896" stroke-width="0.8" stroke-opacity="0.25" stroke-dasharray="4,4"/>
          <line x1="350" y1="90" x2="450" y2="90" stroke="#00c896" stroke-width="0.8" stroke-opacity="0.25" stroke-dasharray="4,4"/>
          <!-- Dot grid -->
          <circle cx="60"  cy="45" r="2" fill="#00d4ff" opacity="0.4"/>
          <circle cx="80"  cy="35" r="1.5" fill="#00d4ff" opacity="0.3"/>
          <circle cx="420" cy="45" r="2" fill="#00c896" opacity="0.4"/>
          <circle cx="400" cy="35" r="1.5" fill="#00c896" opacity="0.3"/>
          <!-- Parameter labels -->
          <text x="40"  y="115" font-size="8" fill="#8bafc7" font-family="sans-serif" opacity="0.7">pH</text>
          <text x="105" y="115" font-size="8" fill="#8bafc7" font-family="sans-serif" opacity="0.7">TDS</text>
          <text x="175" y="115" font-size="8" fill="#8bafc7" font-family="sans-serif" opacity="0.7">Turbidity</text>
          <text x="290" y="115" font-size="8" fill="#8bafc7" font-family="sans-serif" opacity="0.7">Sulfate</text>
          <text x="365" y="115" font-size="8" fill="#8bafc7" font-family="sans-serif" opacity="0.7">THMs</text>
          <text x="420" y="115" font-size="8" fill="#8bafc7" font-family="sans-serif" opacity="0.7">Cl₂</text>
        </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Key statistics row ─────────────────────────────────────────────────────────
st.markdown(divider(), unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
stats = [
    ("3,276", "Water Samples", "Training dataset (CC0)"),
    ("9",     "Parameters Analysed", "WHO-referenced indicators"),
    ("64.2%", "Model Test Accuracy", "Random Forest, 5-fold CV"),
    ("SDG 6", "UN Goal Alignment",   "Clean Water & Sanitation"),
]
for col, (val, label, sub) in zip([c1, c2, c3, c4], stats):
    col.metric(label=label, value=val, help=sub)

st.markdown("<br>", unsafe_allow_html=True)

# ── Feature cards ──────────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Capabilities</h2>',
    unsafe_allow_html=True,
)

fc1, fc2, fc3, fc4 = st.columns(4)

features = [
    (
        "📊",
        "Dataset Dashboard",
        "Explore the 3,276-sample dataset. View feature distributions by potability class, "
        "correlation heatmaps, missing-value analysis, and real model performance metrics.",
    ),
    (
        "🔬",
        "Water Quality Predictor",
        "Enter nine water-quality measurements and receive an instant ML risk assessment "
        "with WHO threshold checks, risk tier classification, and a parameter radar chart.",
    ),
    (
        "📁",
        "Batch Analysis",
        "Upload a CSV of multiple water samples for bulk screening. Download a results "
        "report with risk probabilities, tier labels, and probability distribution charts.",
    ),
    (
        "ℹ",
        "Methodology & About",
        "Full transparency: dataset source and licence, ML pipeline architecture, "
        "honest evaluation metrics, known limitations, and SDG 6 context.",
    ),
]

for col, (icon, title, desc) in zip([fc1, fc2, fc3, fc4], features):
    with col:
        st.markdown(
            f"""
            <div class="aq-feature-card">
                <span class="aq-feature-icon">{icon}</span>
                <p class="aq-feature-title">{title}</p>
                <p class="aq-feature-desc">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)

# ── Parameters section ─────────────────────────────────────────────────────────
st.markdown(divider(), unsafe_allow_html=True)
st.markdown(
    '<h2 class="aq-section-title">Nine Water Quality Parameters</h2>'
    '<p class="aq-section-subtitle">All indicators reference WHO and standard water-quality guidelines</p>',
    unsafe_allow_html=True,
)

params = [
    ("pH",               "6.5 – 8.5",    "Acidity/alkalinity balance"),
    ("Hardness",         "< 300 mg/L",    "Dissolved calcium & magnesium"),
    ("Solids (TDS)",     "< 500 ppm",     "Total dissolved substances"),
    ("Chloramines",      "< 4 ppm",       "Disinfectant residuals"),
    ("Sulfate",          "< 250 mg/L",    "Naturally occurring mineral"),
    ("Conductivity",     "< 400 μS/cm",   "Ionic concentration proxy"),
    ("Organic Carbon",   "< 2 ppm",       "Organic compound load"),
    ("Trihalomethanes",  "< 80 μg/L",     "Chlorination by-products"),
    ("Turbidity",        "< 5 NTU",       "Particle cloudiness"),
]

rows = [params[i:i+3] for i in range(0, len(params), 3)]
for row in rows:
    cols = st.columns(3)
    for col, (name, limit, desc) in zip(cols, row):
        with col:
            st.markdown(
                f"""
                <div class="aq-card" style="padding:1rem 1.25rem;">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                        <div>
                            <p style="font-weight:600; color:#e8f4fd; margin:0; font-size:0.95rem;">{name}</p>
                            <p style="color:#8bafc7; margin:0.2rem 0 0 0; font-size:0.78rem;">{desc}</p>
                        </div>
                        <span class="aq-badge aq-badge-cyan" style="white-space:nowrap; margin-left:0.5rem;">{limit}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("<br style='margin:0.25rem 0;'>", unsafe_allow_html=True)

# ── SDG 6 section ──────────────────────────────────────────────────────────────
st.markdown(divider(), unsafe_allow_html=True)
st.markdown(
    """
    <div class="aq-sdg-block">
        <div style="font-size:2.5rem; margin-bottom:0.75rem;">🌍</div>
        <h2 style="color:#00d4ff; margin:0 0 0.5rem 0; font-size:1.6rem; font-weight:700;">
            UN Sustainable Development Goal 6
        </h2>
        <p style="color:#e8f4fd; font-size:1.05rem; font-weight:500; margin:0 0 0.75rem 0;">
            Clean Water and Sanitation
        </p>
        <p style="color:#8bafc7; max-width:640px; margin:0 auto; font-size:0.9rem; line-height:1.7;">
            Over <strong style="color:#e8f4fd;">2 billion people</strong> worldwide lack access to safely
            managed drinking water. AquaGuard AI demonstrates how machine learning can support
            preliminary water-quality screening — helping communities and researchers identify
            samples that require professional laboratory testing.
        </p>
        <div style="margin-top:1.25rem;">
            <span class="aq-badge aq-badge-cyan">SDG 6.1 — Safe Drinking Water</span>
            &nbsp;
            <span class="aq-badge aq-badge-green">SDG 6.3 — Water Quality</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Tech stack ─────────────────────────────────────────────────────────────────
st.markdown(divider(), unsafe_allow_html=True)
st.markdown(
    '<h2 class="aq-section-title">Technology Stack</h2>',
    unsafe_allow_html=True,
)

tech_cols = st.columns(6)
tech_items = [
    ("Python 3.13",    "Language"),
    ("Streamlit",      "Web UI"),
    ("Scikit-learn",   "Machine Learning"),
    ("Pandas / NumPy", "Data Processing"),
    ("Plotly",         "Visualisation"),
    ("Joblib",         "Model Persistence"),
]
for col, (name, role) in zip(tech_cols, tech_items):
    with col:
        st.markdown(
            f"""
            <div class="aq-card" style="text-align:center; padding:0.9rem 0.75rem;">
                <p style="font-weight:700; color:#00d4ff; margin:0; font-size:0.9rem;">{name}</p>
                <p style="color:#5a7a96; margin:0.2rem 0 0 0; font-size:0.72rem;">{role}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="aq-footer">
        AquaGuard AI &nbsp;·&nbsp; IBM SkillsBuild Machine Learning &amp; Applied AI Internship
        &nbsp;·&nbsp; SDG 6 — Clean Water and Sanitation
        <br>
        <span style="color:#2a4a62; font-size:0.7rem;">
            Dataset: Water Potability by Aditya Kadiwal (CC0) · Kaggle ·
            Predictions are preliminary screening results only and cannot certify water safety.
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
