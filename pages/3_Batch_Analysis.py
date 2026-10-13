"""
pages/3_Batch_Analysis.py
--------------------------
Premium bulk CSV upload and batch risk assessment.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.data_loader import FEATURE_COLS
from src.model import load_model, predict_batch
from src.advisory import classify_risk_tier
from src.styles import get_global_css, disclaimer_bar, divider, PLOTLY_LAYOUT, PLOTLY_LAYOUT_NO_AXES

st.set_page_config(
    page_title="Batch Analysis — AquaGuard AI",
    page_icon="📁",
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
            Batch Water Quality Analysis
        </h1>
        <p style="color:#8bafc7; margin-top:0; font-size:0.95rem;">
            Upload a CSV file containing multiple water samples. Each row is assessed individually
            and you can download a complete risk-assessment report.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Load model ─────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def get_pipeline():
    return load_model()

try:
    pipeline = get_pipeline()
except FileNotFoundError:
    st.markdown(
        '<div class="aq-card" style="border-color:#ff4d6d; text-align:center; padding:2rem;">'
        '<p style="color:#ff4d6d;">No trained model found. Go to the Dashboard page and train the model first.</p>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.stop()

st.markdown(divider(), unsafe_allow_html=True)

# ── Instructions & template ────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Required CSV Format</h2>',
    unsafe_allow_html=True,
)

info_col, dl_col = st.columns([3, 1])

with info_col:
    st.markdown(
        """
        <div class="aq-card" style="padding:1.25rem 1.5rem;">
            <p style="color:#8bafc7; font-size:0.85rem; margin:0 0 0.75rem 0; font-weight:600;
                      text-transform:uppercase; letter-spacing:0.06em;">Required Columns (case-sensitive)</p>
            <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
        """,
        unsafe_allow_html=True,
    )
    col_tags = " ".join(
        f'<span class="aq-badge aq-badge-cyan">{c}</span>'
        for c in FEATURE_COLS
    )
    st.markdown(col_tags + "</div></div>", unsafe_allow_html=True)

with dl_col:
    # Template CSV
    sample_row = {
        "ph": 7.0, "Hardness": 150.0, "Solids": 20000.0,
        "Chloramines": 3.5, "Sulfate": 200.0, "Conductivity": 350.0,
        "Organic_carbon": 10.0, "Trihalomethanes": 60.0, "Turbidity": 3.5,
    }
    template_df  = pd.DataFrame([sample_row])
    csv_template = template_df.to_csv(index=False)
    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        label="Download Template CSV",
        data=csv_template,
        file_name="aquaguard_template.csv",
        mime="text/csv",
        use_container_width=True,
    )

st.markdown(divider(), unsafe_allow_html=True)

# ── File upload area ───────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Upload Samples</h2>',
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Drag and drop your CSV here, or click to browse",
    type=["csv"],
    help="CSV must contain the 9 required columns listed above.",
)

if uploaded_file is None:
    st.markdown(
        """
        <div class="aq-card" style="text-align:center; padding:2.5rem 2rem; border-style:dashed;">
            <p style="font-size:2rem; margin:0 0 0.5rem 0;">📂</p>
            <p style="color:#8bafc7; font-size:0.95rem; margin:0;">
                No file uploaded yet. Use the uploader above to load your water sample data.
            </p>
            <p style="color:#5a7a96; font-size:0.8rem; margin:0.5rem 0 0 0;">
                Accepted format: CSV · Required columns: ph, Hardness, Solids, Chloramines,
                Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    # ── Load and validate ──────────────────────────────────────────────────────
    try:
        input_df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Could not read the uploaded file: {e}")
        st.stop()

    missing_cols = [c for c in FEATURE_COLS if c not in input_df.columns]
    if missing_cols:
        st.markdown(
            f'<div class="aq-card" style="border-color:#ff4d6d;">'
            f'<p style="color:#ff4d6d; font-weight:600;">Missing required columns:</p>'
            f'<p style="color:#8bafc7;">{missing_cols}</p>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.stop()

    st.markdown(
        f'<div style="display:flex; gap:0.5rem; margin-bottom:0.75rem; flex-wrap:wrap;">'
        f'<span class="aq-badge aq-badge-green">Loaded {len(input_df):,} samples</span>'
        f'<span class="aq-badge aq-badge-cyan">{len(input_df.columns)} columns detected</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    with st.expander("Preview uploaded data (first 10 rows)", expanded=False):
        st.dataframe(input_df.head(10), use_container_width=True)

    # ── Run predictions ────────────────────────────────────────────────────────
    with st.spinner("Running batch predictions…"):
        results_df = predict_batch(pipeline, input_df)

    def assign_tier_label(prob):
        tier, _, _ = classify_risk_tier(prob)
        return tier

    def assign_tier_color(prob):
        _, color, _ = classify_risk_tier(prob)
        return color

    results_df["risk_tier"]            = results_df["risk_probability"].apply(assign_tier_label)
    results_df["risk_probability_pct"] = (results_df["risk_probability"] * 100).round(1)
    results_df["predicted_label"]      = results_df["predicted_potability"].map(
        {1: "Potable", 0: "Not Potable"}
    )

    st.markdown(divider(), unsafe_allow_html=True)

    # ── Summary KPIs ──────────────────────────────────────────────────────────
    st.markdown(
        '<h2 class="aq-section-title">Assessment Summary</h2>',
        unsafe_allow_html=True,
    )

    n_high     = int((results_df["risk_probability"] < 0.35).sum())
    n_moderate = int(((results_df["risk_probability"] >= 0.35) & (results_df["risk_probability"] < 0.65)).sum())
    n_low      = int((results_df["risk_probability"] >= 0.65).sum())
    n_potable  = int((results_df["predicted_potability"] == 1).sum())

    kc1, kc2, kc3, kc4 = st.columns(4)
    kc1.metric("High Risk",     f"{n_high:,}",     f"{n_high/len(results_df)*100:.1f}%")
    kc2.metric("Moderate Risk", f"{n_moderate:,}", f"{n_moderate/len(results_df)*100:.1f}%")
    kc3.metric("Low Risk",      f"{n_low:,}",      f"{n_low/len(results_df)*100:.1f}%")
    kc4.metric("Predicted Potable", f"{n_potable:,}", f"{n_potable/len(results_df)*100:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Charts row ─────────────────────────────────────────────────────────────
    chart_c1, chart_c2 = st.columns(2)

    with chart_c1:
        st.markdown(
            '<p style="color:#8bafc7; font-size:0.85rem; font-weight:600; '
            'text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;">Risk Tier Distribution</p>',
            unsafe_allow_html=True,
        )
        tier_data = pd.DataFrame({
            "Risk Tier": ["High Risk", "Moderate Risk", "Low Risk"],
            "Count": [n_high, n_moderate, n_low],
        })
        fig_bar = go.Figure(go.Bar(
            x=tier_data["Risk Tier"],
            y=tier_data["Count"],
            marker=dict(
                color=["#ff4d6d", "#ffb347", "#00c896"],
                line=dict(color="rgba(0,0,0,0)"),
            ),
            text=tier_data["Count"],
            textposition="outside",
            textfont=dict(color="#8bafc7", size=12),
        ))
        fig_bar.update_layout(
            **PLOTLY_LAYOUT,
            height=320,
            showlegend=False,
            yaxis_title="Count",
            xaxis_title="",
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with chart_c2:
        st.markdown(
            '<p style="color:#8bafc7; font-size:0.85rem; font-weight:600; '
            'text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;">Potability Probability Distribution</p>',
            unsafe_allow_html=True,
        )
        fig_hist = px.histogram(
            results_df,
            x="risk_probability_pct",
            nbins=40,
            color_discrete_sequence=["#00d4ff"],
            labels={"risk_probability_pct": "Potability Probability (%)"},
            opacity=0.8,
        )
        fig_hist.add_vline(x=35, line_dash="dash", line_color="#ff4d6d",
                           annotation_text="High/Moderate",
                           annotation_font=dict(color="#ff4d6d", size=10))
        fig_hist.add_vline(x=65, line_dash="dash", line_color="#00c896",
                           annotation_text="Moderate/Low",
                           annotation_font=dict(color="#00c896", size=10))
        fig_hist.update_layout(**PLOTLY_LAYOUT, height=320, yaxis_title="Count")
        st.plotly_chart(fig_hist, use_container_width=True)

    st.markdown(divider(), unsafe_allow_html=True)

    # ── Results table ──────────────────────────────────────────────────────────
    st.markdown(
        '<h2 class="aq-section-title">Full Results</h2>',
        unsafe_allow_html=True,
    )

    display_cols = FEATURE_COLS + ["risk_probability_pct", "risk_tier", "predicted_label"]
    if "Potability" in results_df.columns:
        display_cols.append("Potability")

    st.dataframe(results_df[display_cols].round(4), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Download button ────────────────────────────────────────────────────────
    output_cols = FEATURE_COLS + ["risk_probability", "risk_tier", "predicted_potability"]
    if "Potability" in results_df.columns:
        output_cols.append("Potability")

    csv_output = results_df[output_cols].to_csv(index=False)

    dl_c1, dl_c2, dl_c3 = st.columns([1, 2, 1])
    with dl_c2:
        st.download_button(
            label="Download Full Results CSV",
            data=csv_output,
            file_name="aquaguard_results.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary",
        )
    st.markdown(
        '<p style="text-align:center; color:#5a7a96; font-size:0.78rem; margin-top:0.5rem;">'
        'Downloaded CSV includes risk_probability, risk_tier, and predicted_potability columns.</p>',
        unsafe_allow_html=True,
    )

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="aq-footer">
        AquaGuard AI · Batch Analysis · IBM SkillsBuild ML &amp; Applied AI Internship · SDG 6
    </div>
    """,
    unsafe_allow_html=True,
)
