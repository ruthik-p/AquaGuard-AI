"""
pages/1_Dashboard.py
---------------------
Premium dataset explorer and model performance dashboard.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np

from src.data_loader import load_raw_data, FEATURE_COLS, TARGET_COL
from src.model import load_model, MODEL_PATH, train_and_save
from src.styles import get_global_css, disclaimer_bar, divider, PLOTLY_LAYOUT, PLOTLY_LAYOUT_NO_AXES

st.set_page_config(
    page_title="Dashboard — AquaGuard AI",
    page_icon="📊",
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
            Dataset Dashboard
        </h1>
        <p style="color:#8bafc7; margin-top:0; font-size:0.95rem;">
            Explore the water-potability training dataset and review actual model evaluation metrics.
            All metrics are computed on held-out data — no cherry-picking.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Load data ──────────────────────────────────────────────────────────────────
with st.spinner("Loading dataset…"):
    df = load_raw_data()

st.markdown(divider(), unsafe_allow_html=True)

# ── Dataset KPI row ────────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Dataset Overview</h2>',
    unsafe_allow_html=True,
)

potable_pct   = df[TARGET_COL].mean() * 100
missing_total = int(df.isnull().sum().sum())

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Samples",    f"{len(df):,}")
c2.metric("Features",         str(len(FEATURE_COLS)))
c3.metric("Potable",          f"{int(df[TARGET_COL].sum()):,}", f"{potable_pct:.1f}%")
c4.metric("Not Potable",      f"{int((df[TARGET_COL]==0).sum()):,}", f"{100-potable_pct:.1f}%")
c5.metric("Missing Values",   f"{missing_total:,}", "in ph, Sulfate, THMs")

st.markdown("<br>", unsafe_allow_html=True)

# ── Summary stats table ────────────────────────────────────────────────────────
with st.expander("Summary Statistics", expanded=False):
    st.dataframe(df[FEATURE_COLS].describe().round(3), use_container_width=True)

st.markdown(divider(), unsafe_allow_html=True)

# ── Distribution & class balance row ──────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Data Distribution</h2>',
    unsafe_allow_html=True,
)

col_a, col_b = st.columns([1, 1])

with col_a:
    st.markdown(
        '<p style="color:#8bafc7; font-size:0.85rem; font-weight:600; '
        'text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;">Class Balance</p>',
        unsafe_allow_html=True,
    )
    class_counts = df[TARGET_COL].value_counts().reset_index()
    class_counts.columns = ["Potability", "Count"]
    class_counts["Label"] = class_counts["Potability"].map({0: "Not Potable", 1: "Potable"})
    fig_pie = px.pie(
        class_counts, values="Count", names="Label",
        color="Label",
        color_discrete_map={"Potable": "#00c896", "Not Potable": "#ff4d6d"},
        hole=0.55,
    )
    fig_pie.update_traces(
        textinfo="percent+label",
        textfont=dict(color="#e8f4fd"),
        marker=dict(line=dict(color="#0d1b2e", width=2)),
    )
    fig_pie.update_layout(
        **PLOTLY_LAYOUT_NO_AXES,
        height=320,
        showlegend=False,
        annotations=[dict(
            text=f"{len(df):,}<br>samples",
            x=0.5, y=0.5,
            font=dict(size=14, color="#e8f4fd"),
            showarrow=False,
        )],
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col_b:
    st.markdown(
        '<p style="color:#8bafc7; font-size:0.85rem; font-weight:600; '
        'text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;">Missing Values per Feature</p>',
        unsafe_allow_html=True,
    )
    missing = df[FEATURE_COLS].isnull().sum().reset_index()
    missing.columns = ["Feature", "Missing Count"]
    fig_miss = px.bar(
        missing, x="Feature", y="Missing Count",
        color="Missing Count",
        color_continuous_scale=[[0, "#1a3a5c"], [0.5, "#00a8cc"], [1, "#ff4d6d"]],
        text="Missing Count",
    )
    fig_miss.update_traces(textposition="outside", textfont=dict(color="#8bafc7", size=11))
    fig_miss.update_layout(
        **PLOTLY_LAYOUT,
        coloraxis_showscale=False,
        xaxis_tickangle=-30,
        height=320,
    )
    st.plotly_chart(fig_miss, use_container_width=True)

st.markdown(divider(), unsafe_allow_html=True)

# ── Feature distributions ──────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Feature Distributions by Potability</h2>',
    unsafe_allow_html=True,
)

feat_cols = st.columns([2, 1])
with feat_cols[0]:
    selected_feature = st.selectbox(
        "Select parameter to explore:",
        FEATURE_COLS,
        index=0,
        key="feature_selector",
    )
with feat_cols[1]:
    chart_type = st.radio(
        "Chart type:",
        ["Histogram", "Box plot"],
        horizontal=True,
        key="chart_type_radio",
    )

df_plot = df[[selected_feature, TARGET_COL]].dropna()
df_plot = df_plot.copy()
df_plot["Label"] = df_plot[TARGET_COL].map({0: "Not Potable", 1: "Potable"})

if chart_type == "Histogram":
    fig_dist = px.histogram(
        df_plot, x=selected_feature, color="Label",
        barmode="overlay", nbins=50, opacity=0.75,
        color_discrete_map={"Potable": "#00c896", "Not Potable": "#ff4d6d"},
    )
    fig_dist.update_layout(**PLOTLY_LAYOUT, height=360, legend_title_text="")
else:
    fig_dist = px.box(
        df_plot, x="Label", y=selected_feature, color="Label",
        color_discrete_map={"Potable": "#00c896", "Not Potable": "#ff4d6d"},
    )
    fig_dist.update_layout(**PLOTLY_LAYOUT, height=360, legend_title_text="", showlegend=False)

st.plotly_chart(fig_dist, use_container_width=True)

st.markdown(divider(), unsafe_allow_html=True)

# ── Correlation heatmap ────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Feature Correlation Heatmap</h2>',
    unsafe_allow_html=True,
)
corr = df[FEATURE_COLS].corr().round(2)
fig_heat = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale=[[0, "#ff4d6d"], [0.5, "#0d1b2e"], [1, "#00d4ff"]],
    zmin=-1, zmax=1,
)
fig_heat.update_traces(textfont=dict(size=11, color="#e8f4fd"))
fig_heat.update_layout(
    **PLOTLY_LAYOUT,
    height=480,
    xaxis_tickangle=-30,
    coloraxis_colorbar=dict(
        tickfont=dict(color="#8bafc7"),
        title=dict(text="r", font=dict(color="#8bafc7")),
    ),
)
st.plotly_chart(fig_heat, use_container_width=True)

st.markdown(divider(), unsafe_allow_html=True)

# ── Model performance ──────────────────────────────────────────────────────────
st.markdown(
    '<h2 class="aq-section-title">Model Performance</h2>'
    '<p class="aq-section-subtitle">'
    'Random Forest Classifier · 5-fold stratified CV · 20% held-out test set · '
    'Metrics are actual values — no cherry-picking or rounding up.'
    '</p>',
    unsafe_allow_html=True,
)

if not os.path.exists(MODEL_PATH):
    st.markdown(
        '<div class="aq-card" style="border-color:#ffb347; text-align:center; padding:2rem;">'
        '<p style="color:#ffb347; font-size:1rem;">No trained model found.</p>'
        '</div>',
        unsafe_allow_html=True,
    )
    if st.button("Train Model Now", type="primary"):
        with st.spinner("Training Random Forest — approximately 30 seconds…"):
            metrics = train_and_save(df)
        st.session_state["metrics"] = metrics
        st.success("Model trained and saved!")
        st.rerun()
else:
    # Bootstrap metrics from saved model if not in session
    if "metrics" not in st.session_state:
        try:
            pipeline = load_model()
            importances = dict(zip(
                FEATURE_COLS,
                pipeline.named_steps["classifier"].feature_importances_.tolist()
            ))
            st.session_state["metrics"] = {"feature_importances": importances}
        except Exception as e:
            st.error(f"Could not load model: {e}")

    metrics = st.session_state.get("metrics", {})

    if metrics:
        # ── Metric cards ───────────────────────────────────────────────────────
        if "cv_accuracy_mean" in metrics:
            m1, m2, m3, m4 = st.columns(4)
            m1.metric(
                "CV Accuracy (5-fold)",
                f"{metrics['cv_accuracy_mean']:.3f}",
                f"± {metrics['cv_accuracy_std']:.3f}",
            )
            m2.metric(
                "CV F1 Macro (5-fold)",
                f"{metrics['cv_f1_mean']:.3f}",
                f"± {metrics['cv_f1_std']:.3f}",
            )
            m3.metric("Test Set Accuracy", f"{metrics['test_accuracy']:.3f}")
            m4.metric("Test Set F1 Macro", f"{metrics['test_f1_macro']:.3f}")
            st.markdown("<br>", unsafe_allow_html=True)

        # ── Feature importance ─────────────────────────────────────────────────
        if "feature_importances" in metrics:
            fi_col, cm_col = st.columns([3, 2])

            with fi_col:
                st.markdown(
                    '<p style="color:#8bafc7; font-size:0.85rem; font-weight:600; '
                    'text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;">'
                    'Feature Importances</p>',
                    unsafe_allow_html=True,
                )
                fi = pd.DataFrame(
                    list(metrics["feature_importances"].items()),
                    columns=["Feature", "Importance"],
                ).sort_values("Importance", ascending=True)

                fig_fi = go.Figure(go.Bar(
                    x=fi["Importance"],
                    y=fi["Feature"],
                    orientation="h",
                    marker=dict(
                        color=fi["Importance"],
                        colorscale=[[0, "#1a3a5c"], [0.5, "#0099cc"], [1, "#00d4ff"]],
                        line=dict(color="rgba(0,0,0,0)"),
                    ),
                    text=[f"{v:.3f}" for v in fi["Importance"]],
                    textposition="outside",
                    textfont=dict(color="#8bafc7", size=11),
                ))
                fig_fi.update_layout(
                    **PLOTLY_LAYOUT,
                    height=380,
                    xaxis_title="Importance Score",
                    yaxis_title="",
                )
                st.plotly_chart(fig_fi, use_container_width=True)

            # ── Confusion matrix ───────────────────────────────────────────────
            
            # ── Confusion matrix ───────────────────────────────────────────────
            if "confusion_matrix" in metrics:
                with cm_col:
                    st.markdown(
                        '<p style="color:#8bafc7; font-size:0.85rem; font-weight:600; '
                        'text-transform:uppercase; letter-spacing:0.06em; margin-bottom:0.5rem;">'
                        'Confusion Matrix (Test Set)</p>',
                        unsafe_allow_html=True,
                    )

                    cm = metrics["confusion_matrix"]

                    fig_cm = go.Figure(
                        data=go.Heatmap(
                            z=cm,
                            x=["Predicted Not Potable", "Predicted Potable"],
                            y=["Actual Not Potable", "Actual Potable"],
                            colorscale="Blues",
                            text=cm,
                            texttemplate="%{text}",
                            showscale=True,
                        )
                    )

                    fig_cm.update_layout(
                        title="Confusion Matrix (Test Set)",
                        xaxis_title="Predicted Label",
                        yaxis_title="Actual Label",
                        template="plotly_dark",
                    )

                    st.plotly_chart(
                        fig_cm,
                        use_container_width=True,
                    )


        # ── Classification report ──────────────────────────────────────────────
        if "classification_report" in metrics:
            with st.expander("Full Classification Report", expanded=False):
                st.code(metrics["classification_report"], language="text")

        # ── Retrain option ─────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Re-train Model to Refresh Metrics", type="secondary"):
            with st.spinner("Training…"):
                metrics = train_and_save(df)
            st.session_state["metrics"] = metrics
            st.success("Model retrained and metrics updated.")
            st.rerun()

    else:
        st.markdown(
            '<div class="aq-card" style="text-align:center; padding:2rem;">'
            '<p style="color:#8bafc7;">Model loaded. Retrain to see full metrics.</p>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Train to Get Full Metrics", type="primary"):
            with st.spinner("Training…"):
                metrics = train_and_save(df)
            st.session_state["metrics"] = metrics
            st.rerun()

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="aq-footer">
        AquaGuard AI · Dashboard · IBM SkillsBuild ML &amp; Applied AI Internship · SDG 6
    </div>
    """,
    unsafe_allow_html=True,
)
