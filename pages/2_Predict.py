"""
pages/2_Predict.py
------------------
Premium single-sample water quality prediction with risk advisory.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

from src.data_loader import load_raw_data, FEATURE_COLS
from src.model import load_model, predict_single
from src.advisory import get_advisory, WHO_THRESHOLDS
from src.preprocessing import get_feature_medians
from src.styles import get_global_css, disclaimer_bar, divider, PLOTLY_LAYOUT, PLOTLY_LAYOUT_NO_AXES

st.set_page_config(
    page_title="Predict — AquaGuard AI",
    page_icon="🔬",
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
            Water Quality Predictor
        </h1>
        <p style="color:#8bafc7; margin-top:0; font-size:0.95rem;">
            Enter the nine water-quality measurements below. The Random Forest model will
            estimate potability risk and check each parameter against WHO guideline thresholds.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Load model and dataset defaults ────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def get_pipeline():
    return load_model()

@st.cache_data(show_spinner=False)
def get_defaults():
    df = load_raw_data()
    return get_feature_medians(df)

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

defaults = get_defaults()

# ── WHO threshold reference lookup ─────────────────────────────────────────────
WHO_DISPLAY = {
    "ph":              ("pH",                    "Safe: 6.5 – 8.5"),
    "Hardness":        ("Hardness",              "Safe: < 300 mg/L"),
    "Solids":          ("Total Dissolved Solids","Safe: < 500 ppm"),
    "Chloramines":     ("Chloramines",           "Safe: < 4 ppm"),
    "Sulfate":         ("Sulfate",               "Safe: < 250 mg/L"),
    "Conductivity":    ("Conductivity",          "Safe: < 400 μS/cm"),
    "Organic_carbon":  ("Organic Carbon",        "Safe: < 2 ppm"),
    "Trihalomethanes": ("Trihalomethanes (THMs)","Safe: < 80 μg/L"),
    "Turbidity":       ("Turbidity",             "Safe: < 5 NTU"),
}

SLIDER_CONFIG = {
    "ph":               (0.0,    14.0,   0.07),
    "Hardness":         (0.0,    600.0,  3.0),
    "Solids":           (0.0,    60000.0,300.0),
    "Chloramines":      (0.0,    15.0,   0.075),
    "Sulfate":          (0.0,    600.0,  3.0),
    "Conductivity":     (100.0,  800.0,  3.5),
    "Organic_carbon":   (0.0,    30.0,   0.15),
    "Trihalomethanes":  (0.0,    130.0,  0.65),
    "Turbidity":        (0.0,    10.0,   0.05),
}

# ── Input form ─────────────────────────────────────────────────────────────────
st.markdown(divider(), unsafe_allow_html=True)
st.markdown(
    '<h2 class="aq-section-title">Water Quality Measurements</h2>'
    '<p class="aq-section-subtitle">Adjust each parameter — defaults are set to dataset medians</p>',
    unsafe_allow_html=True,
)

input_values = {}

# Render in a 3-column grid (3+3+3 = 9 features)
feat_groups = [FEATURE_COLS[i:i+3] for i in range(0, 9, 3)]

for group in feat_groups:
    cols = st.columns(3)
    for col, feat in zip(cols, group):
        lo, hi, step = SLIDER_CONFIG[feat]
        label, who_note = WHO_DISPLAY[feat]
        default_val = float(np.clip(round(defaults.get(feat, (lo + hi) / 2), 4), lo, hi))

        # Colour code the WHO note based on whether the default is within safe range
        thr = WHO_THRESHOLDS[feat]
        safe_min = thr.get("safe_min")
        safe_max = thr.get("safe_max")
        in_range = (safe_min is None or default_val >= safe_min) and \
                   (safe_max is None or default_val <= safe_max)
        note_color = "#00c896" if in_range else "#ffb347"

        with col:
            st.markdown(
                f'<p class="aq-param-label">{label}</p>'
                f'<p class="aq-param-who" style="color:{note_color};">{who_note}</p>',
                unsafe_allow_html=True,
            )
            input_values[feat] = st.slider(
                label,
                min_value=float(lo),
                max_value=float(hi),
                value=default_val,
                step=float(step),
                key=f"slider_{feat}",
                label_visibility="collapsed",
            )

    st.markdown("<div style='margin-bottom:0.25rem;'></div>", unsafe_allow_html=True)

st.markdown(divider(), unsafe_allow_html=True)

# ── Live parameter status bar ──────────────────────────────────────────────────
status_items = []
for feat in FEATURE_COLS:
    thr = WHO_THRESHOLDS[feat]
    val = input_values[feat]
    s_min = thr.get("safe_min")
    s_max = thr.get("safe_max")
    in_range = (s_min is None or val >= s_min) and (s_max is None or val <= s_max)
    label_short = WHO_DISPLAY[feat][0].split(" ")[0]
    color   = "#00c896" if in_range else "#ff4d6d"
    bg      = "rgba(0,200,150,0.12)" if in_range else "rgba(255,77,109,0.12)"
    symbol  = "✓" if in_range else "✕"
    status_items.append(
        f'<span style="background:{bg}; border:1px solid {color}; '
        f'border-radius:20px; padding:0.2rem 0.65rem; font-size:0.75rem; '
        f'font-weight:600; color:{color}; white-space:nowrap;">'
        f'{symbol} {label_short}</span>'
    )

st.markdown(
    '<p style="color:#8bafc7; font-size:0.8rem; font-weight:600; '
    'text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.5rem;">'
    'WHO Threshold Status</p>'
    '<div style="display:flex; flex-wrap:wrap; gap:0.4rem;">'
    + " ".join(status_items) +
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ── Predict button ─────────────────────────────────────────────────────────────
predict_btn = st.button(
    "Analyse Water Quality",
    type="primary",
    use_container_width=True,
)

if predict_btn:
    with st.spinner("Running analysis…"):
        prob, pred = predict_single(pipeline, input_values)
        advisory   = get_advisory(prob, input_values)

    st.markdown(divider(), unsafe_allow_html=True)

    # ── Risk tier card ─────────────────────────────────────────────────────────
    tier_class = {
        "High Risk":     "aq-risk-high",
        "Moderate Risk": "aq-risk-moderate",
        "Low Risk":      "aq-risk-low",
    }.get(advisory.risk_tier, "aq-risk-low")

    tier_color_hex = {
        "High Risk":     "#ff4d6d",
        "Moderate Risk": "#ffb347",
        "Low Risk":      "#00c896",
    }.get(advisory.risk_tier, "#00c896")

    tier_icon = {
        "High Risk":     "⛔",
        "Moderate Risk": "⚠",
        "Low Risk":      "✓",
    }.get(advisory.risk_tier, "✓")

    potable_label = "Potable" if pred == 1 else "Not Potable"
    potable_color = "#00c896" if pred == 1 else "#ff4d6d"

    st.markdown(
        f"""
        <div class="{tier_class} aq-animate-up">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
                <div>
                    <p class="aq-risk-title" style="color:{tier_color_hex};">
                        {tier_icon}&nbsp; {advisory.risk_tier}
                    </p>
                    <p class="aq-risk-subtitle">
                        Potability probability: <strong style="color:{tier_color_hex};">{prob*100:.1f}%</strong>
                        &nbsp;|&nbsp;
                        Predicted class: <strong style="color:{potable_color};">{potable_label}</strong>
                    </p>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:3.5rem; font-weight:800; color:{tier_color_hex};
                                line-height:1; font-variant-numeric:tabular-nums;">
                        {prob*100:.0f}%
                    </div>
                    <div style="font-size:0.75rem; color:#5a7a96; margin-top:0.2rem;">
                        Potability confidence
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    result_col, radar_col = st.columns([1, 1])

    with result_col:
        # ── WHO violations ─────────────────────────────────────────────────────
        st.markdown(
            '<h2 class="aq-section-title" style="font-size:1.1rem;">Parameter Assessment</h2>',
            unsafe_allow_html=True,
        )

        if advisory.violations:
            st.markdown(
                f'<p style="color:#8bafc7; font-size:0.85rem;">'
                f'{len(advisory.violations)} parameter(s) outside WHO guidelines:</p>',
                unsafe_allow_html=True,
            )
            for v in advisory.violations:
                direction_str = "below" if v["direction"] == "below" else "above"
                unit = f" {v['unit']}" if v["unit"] else ""
                st.markdown(
                    f"""
                    <div class="aq-violation">
                        <div class="aq-violation-title">
                            {v['label']}: {v['value']:.3f}{unit}
                        </div>
                        <div class="aq-violation-text">
                            {direction_str.capitalize()} safe limit of {v['limit']}{unit}.
                            {v['advice'] or ''}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                '<div class="aq-step" style="background:rgba(0,200,150,0.1);">'
                '<strong style="color:#00c896;">All measured parameters are within WHO guideline ranges.</strong>'
                '</div>',
                unsafe_allow_html=True,
            )

        # ── Next steps ─────────────────────────────────────────────────────────
        st.markdown(
            '<h2 class="aq-section-title" style="font-size:1.1rem; margin-top:1.25rem;">Recommended Actions</h2>',
            unsafe_allow_html=True,
        )
        for step in advisory.next_steps:
            st.markdown(
                f'<div class="aq-step">{step}</div>',
                unsafe_allow_html=True,
            )

    with radar_col:
        # ── Radar chart ────────────────────────────────────────────────────────
        st.markdown(
            '<h2 class="aq-section-title" style="font-size:1.1rem;">Parameter Radar</h2>'
            '<p class="aq-section-subtitle">Your values vs WHO safe upper limits (100% line)</p>',
            unsafe_allow_html=True,
        )

        radar_features = [f for f in FEATURE_COLS if WHO_THRESHOLDS[f]["safe_max"]]
        safe_maxes = [WHO_THRESHOLDS[f]["safe_max"] for f in radar_features]
        user_vals  = [input_values[f] for f in radar_features]

        norm_user = [min(v / m * 100, 180) if m else 0 for v, m in zip(user_vals, safe_maxes)]
        norm_safe = [100] * len(radar_features)
        labels    = [WHO_THRESHOLDS[f]["label"] for f in radar_features]

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=norm_safe + [norm_safe[0]],
            theta=labels + [labels[0]],
            mode="lines",
            line=dict(color="#ff4d6d", dash="dash", width=1.5),
            name="WHO Safe Limit",
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=norm_user + [norm_user[0]],
            theta=labels + [labels[0]],
            fill="toself",
            fillcolor="rgba(0,212,255,0.12)",
            line=dict(color="#00d4ff", width=2),
            name="Your Sample",
        ))
        radar_layout = dict(PLOTLY_LAYOUT_NO_AXES)
        radar_layout["legend"] = dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#8bafc7", size=11),
            orientation="h",
            y=-0.12,
        )
        fig_radar.update_layout(
            **radar_layout,
            polar=dict(
                bgcolor="rgba(13,27,46,0.5)",
                radialaxis=dict(
                    visible=True,
                    range=[0, 180],
                    gridcolor="#1a3a5c",
                    tickfont=dict(color="#5a7a96", size=9),
                    ticksuffix="%",
                ),
                angularaxis=dict(
                    tickfont=dict(color="#8bafc7", size=10),
                    gridcolor="#1a3a5c",
                ),
            ),
            showlegend=True,
            height=420,
        )
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown(
            '<p style="color:#5a7a96; font-size:0.72rem; text-align:center;">'
            'Values above 100% exceed the WHO safe upper limit.</p>',
            unsafe_allow_html=True,
        )

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="aq-footer">
        AquaGuard AI · Predictor · IBM SkillsBuild ML &amp; Applied AI Internship · SDG 6
    </div>
    """,
    unsafe_allow_html=True,
)
