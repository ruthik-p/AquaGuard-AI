"""
src/styles.py
-------------
Shared CSS and styling utilities for AquaGuard AI.
Inject into any page with: st.markdown(get_global_css(), unsafe_allow_html=True)
"""

# ── Colour palette ─────────────────────────────────────────────────────────────
PALETTE = {
    "navy_deep":    "#0a0f1e",
    "navy_mid":     "#0d1b2e",
    "navy_card":    "#0f2035",
    "navy_border":  "#1a3a5c",
    "cyan":         "#00d4ff",
    "cyan_dim":     "#00a8cc",
    "aqua":         "#0099cc",
    "emerald":      "#00c896",
    "emerald_dim":  "#00a07a",
    "white":        "#e8f4fd",
    "muted":        "#8bafc7",
    "danger":       "#ff4d6d",
    "warning":      "#ffb347",
    "success":      "#00c896",
}

# Plotly dark template colours for consistent charts
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(13,27,46,0.6)",
    font=dict(color="#e8f4fd", family="sans-serif"),
    title_font=dict(color="#e8f4fd", size=16),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#e8f4fd")),
    xaxis=dict(gridcolor="#1a3a5c", linecolor="#1a3a5c", tickfont=dict(color="#8bafc7")),
    yaxis=dict(gridcolor="#1a3a5c", linecolor="#1a3a5c", tickfont=dict(color="#8bafc7")),
    margin=dict(t=40, b=40, l=40, r=20),
)

PLOTLY_LAYOUT_NO_AXES = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#e8f4fd", family="sans-serif"),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#e8f4fd")),
    margin=dict(t=20, b=20, l=20, r=20),
)


def get_global_css() -> str:
    """Return the full <style> block injected on every page."""
    return """
<style>
/* ── Reset & base ──────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* ── Hide default Streamlit chrome ─────────────────────────────────────────── */

/* ── Hide default Streamlit chrome ─────────────────────────────────────────── */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Keep Streamlit toolbar and sidebar controls accessible */
header [data-testid="stToolbar"] {
    visibility: visible !important;
    opacity: 1 !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

[data-testid="stSidebarCollapsedControl"],
[data-testid="stSidebarCollapseButton"] {
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
}

/* ── Main container ────────────────────────────────────────────────────────── */
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* ── Sidebar ───────────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0f1e 0%, #0d1b2e 100%);
    border-right: 1px solid #1a3a5c;
}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] label {
    color: #8bafc7 !important;
}

/* ── Card component ────────────────────────────────────────────────────────── */
.aq-card {
    background: linear-gradient(135deg, #0f2035 0%, #0d1b2e 100%);
    border: 1px solid #1a3a5c;
    border-radius: 16px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.aq-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(0, 212, 255, 0.08);
}

/* ── Metric card ───────────────────────────────────────────────────────────── */
.aq-metric {
    background: linear-gradient(135deg, #0f2035 0%, #0d1b2e 100%);
    border: 1px solid #1a3a5c;
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.aq-metric:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 24px rgba(0, 212, 255, 0.12);
}
.aq-metric-value {
    font-size: 2rem;
    font-weight: 700;
    color: #00d4ff;
    line-height: 1.1;
    margin: 0.25rem 0;
}
.aq-metric-label {
    font-size: 0.8rem;
    font-weight: 500;
    color: #8bafc7;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin: 0;
}
.aq-metric-sub {
    font-size: 0.75rem;
    color: #5a7a96;
    margin-top: 0.2rem;
}

/* ── Section heading ───────────────────────────────────────────────────────── */
.aq-section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #e8f4fd;
    margin: 1.5rem 0 0.75rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #1a3a5c;
}
.aq-section-subtitle {
    font-size: 0.9rem;
    color: #8bafc7;
    margin-top: -0.5rem;
    margin-bottom: 1rem;
}

/* ── Risk tier result cards ────────────────────────────────────────────────── */
.aq-risk-high {
    background: linear-gradient(135deg, rgba(255,77,109,0.12) 0%, rgba(15,32,53,1) 60%);
    border: 2px solid #ff4d6d;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 1rem 0;
}
.aq-risk-moderate {
    background: linear-gradient(135deg, rgba(255,179,71,0.12) 0%, rgba(15,32,53,1) 60%);
    border: 2px solid #ffb347;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 1rem 0;
}
.aq-risk-low {
    background: linear-gradient(135deg, rgba(0,200,150,0.12) 0%, rgba(15,32,53,1) 60%);
    border: 2px solid #00c896;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 1rem 0;
}
.aq-risk-title {
    font-size: 1.8rem;
    font-weight: 800;
    margin: 0 0 0.4rem 0;
    line-height: 1.1;
}
.aq-risk-subtitle {
    font-size: 1rem;
    color: #8bafc7;
    margin: 0;
}

/* ── Tag / badge ───────────────────────────────────────────────────────────── */
.aq-badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.aq-badge-cyan   { background: rgba(0,212,255,0.15); color: #00d4ff; border: 1px solid rgba(0,212,255,0.3); }
.aq-badge-green  { background: rgba(0,200,150,0.15); color: #00c896; border: 1px solid rgba(0,200,150,0.3); }
.aq-badge-red    { background: rgba(255,77,109,0.15); color: #ff4d6d; border: 1px solid rgba(255,77,109,0.3); }
.aq-badge-orange { background: rgba(255,179,71,0.15); color: #ffb347; border: 1px solid rgba(255,179,71,0.3); }

/* ── Disclaimer bar ────────────────────────────────────────────────────────── */
.aq-disclaimer {
    background: rgba(255, 179, 71, 0.08);
    border: 1px solid rgba(255, 179, 71, 0.3);
    border-radius: 10px;
    padding: 0.75rem 1.25rem;
    font-size: 0.82rem;
    color: #ffb347;
    margin-bottom: 1.5rem;
    line-height: 1.5;
}

/* ── Hero section ──────────────────────────────────────────────────────────── */

/* Hero section */
.aq-hero {
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    padding: 2.5rem 1.25rem 1.5rem;
    text-align: center;
    box-sizing: border-box;
}

.aq-hero-title {
    max-width: 780px;
    margin: 0 auto 0.75rem;
    font-size: clamp(2rem, 4vw, 3.2rem);
    font-weight: 800;
    background: linear-gradient(135deg, #00d4ff 0%, #0099cc 50%, #00c896 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
    text-align: center;
}


.aq-hero-subtitle {
    width: 100%;
    text-align: center;
    font-size: 1.2rem;
    color: #8bafc7;
    margin: 0 auto 0.75rem;
}


/* Center the subtitle and description inside the full hero section */
.aq-hero .aq-hero-subtitle,
.aq-hero .aq-hero-desc {
    display: block !important;
    width: 100% !important;
    max-width: 680px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    text-align: center !important;
    box-sizing: border-box !important;
}

.aq-hero .aq-hero-subtitle {
    margin-top: 0;
    margin-bottom: 0.75rem;
}

.aq-hero .aq-hero-desc {
    margin-top: 0.75rem;
    margin-bottom: 1.5rem;
    line-height: 1.8;
}




/* ── Feature card for landing ──────────────────────────────────────────────── */
.aq-feature-card {
    background: linear-gradient(135deg, #0f2035 0%, #0d1b2e 100%);
    border: 1px solid #1a3a5c;
    border-radius: 16px;
    padding: 1.75rem 1.5rem;
    height: 100%;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}
.aq-feature-card:hover {
    transform: translateY(-4px);
    border-color: #00d4ff;
    box-shadow: 0 12px 40px rgba(0, 212, 255, 0.12);
}
.aq-feature-icon {
    font-size: 2rem;
    margin-bottom: 0.75rem;
    display: block;
}
.aq-feature-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e8f4fd;
    margin: 0 0 0.5rem 0;
}
.aq-feature-desc {
    font-size: 0.88rem;
    color: #8bafc7;
    line-height: 1.6;
    margin: 0;
}

/* ── SDG section ───────────────────────────────────────────────────────────── */
.aq-sdg-block {
    background: linear-gradient(135deg, rgba(0,152,204,0.15) 0%, rgba(0,200,150,0.08) 100%);
    border: 1px solid rgba(0,212,255,0.25);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin: 1.5rem 0;
}

/* ── Parameter input row ───────────────────────────────────────────────────── */
.aq-param-label {
    font-size: 0.78rem;
    font-weight: 600;
    color: #8bafc7;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.2rem;
}
.aq-param-who {
    font-size: 0.72rem;
    color: #5a7a96;
    margin-top: -0.5rem;
    margin-bottom: 0.5rem;
}

/* ── Violation item ────────────────────────────────────────────────────────── */
.aq-violation {
    background: rgba(255,77,109,0.07);
    border-left: 3px solid #ff4d6d;
    border-radius: 0 8px 8px 0;
    padding: 0.6rem 1rem;
    margin-bottom: 0.5rem;
    font-size: 0.88rem;
}
.aq-violation-title {
    font-weight: 600;
    color: #ff4d6d;
}
.aq-violation-text {
    color: #8bafc7;
    margin-top: 0.1rem;
}

/* ── Step item ─────────────────────────────────────────────────────────────── */
.aq-step {
    background: rgba(0,200,150,0.06);
    border-left: 3px solid #00c896;
    border-radius: 0 8px 8px 0;
    padding: 0.6rem 1rem;
    margin-bottom: 0.5rem;
    font-size: 0.88rem;
    color: #b0d8c8;
}

/* ── Separator ─────────────────────────────────────────────────────────────── */
.aq-divider {
    border: none;
    border-top: 1px solid #1a3a5c;
    margin: 1.5rem 0;
}

/* ── Premium animations ───────────────────────────────────────────────────── */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(22px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}

@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 0 rgba(0,212,255,0); }
    50% { box-shadow: 0 0 22px rgba(0,212,255,0.20); }
}

@keyframes water-shimmer {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.aq-animate-up {
    animation: fadeInUp 0.65s ease both;
}

.aq-animate-in {
    animation: fadeIn 0.6s ease both;
}

.aq-pulse-glow {
    animation: pulse-glow 3s ease-in-out infinite;
}

/* ── Premium glass cards ──────────────────────────────────────────────────── */
.aq-card,
.aq-feature-card,
.aq-metric {
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.aq-card,
.aq-feature-card {
    position: relative;
    overflow: hidden;
}

.aq-card::before,
.aq-feature-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00d4ff, #00c896, transparent);
    background-size: 200% 100%;
    opacity: 0.65;
    transition: opacity 0.3s ease;
}

.aq-card:hover::before,
.aq-feature-card:hover::before {
    opacity: 1;
    animation: water-shimmer 3s linear infinite;
}

.aq-card:hover,
.aq-feature-card:hover,
.aq-metric:hover {
    border-color: rgba(0,212,255,0.55);
    box-shadow: 0 12px 35px rgba(0,212,255,0.10);
}

/* ── Modern section headings ──────────────────────────────────────────────── */
.aq-section-title {
    letter-spacing: -0.025em;
    position: relative;
}

.aq-section-title::after {
    content: "";
    display: block;
    width: 64px;
    height: 3px;
    margin-top: 9px;
    border-radius: 5px;
    background: linear-gradient(90deg, #00d4ff, #00c896);
}

/* ── Polished hero title ──────────────────────────────────────────────────── */
.aq-hero-title {
    background-size: 200% auto;
    animation: water-shimmer 7s ease infinite;
}

/* ── Better buttons ───────────────────────────────────────────────────────── */
.stButton > button {
    border-radius: 12px !important;
    padding: 0.55rem 1.1rem !important;
    font-weight: 600 !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease,
                border-color 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    border-color: #00d4ff !important;
}

/* ── Smoother inputs ──────────────────────────────────────────────────────── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] {
    border-radius: 10px !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

/* ── Refined sidebar ──────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    box-shadow: 8px 0 30px rgba(0,0,0,0.12);
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    line-height: 1.65;
}

/* ── Accessible motion ────────────────────────────────────────────────────── */
@media (prefers-reduced-motion: reduce) {
    .aq-animate-up,
    .aq-animate-in,
    .aq-pulse-glow,
    .aq-hero-title {
        animation: none !important;
    }

    .aq-card,
    .aq-feature-card,
    .aq-metric,
    .stButton > button {
        transition: none !important;
    }
}

/* ── Footer ────────────────────────────────────────────────────────────────── */
.aq-footer {
    text-align: center;
    font-size: 0.78rem;
    color: #3a5a76;
    padding: 1.5rem 0 0.5rem 0;
    border-top: 1px solid #1a3a5c;
    margin-top: 2rem;
}

/* ── Streamlit widget overrides ────────────────────────────────────────────── */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #0f2035 0%, #0d1b2e 100%);
    border: 1px solid #1a3a5c;
    border-radius: 14px;
    padding: 1rem 1.25rem;
    transition: transform 0.2s ease;
}
div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    border-color: rgba(0,212,255,0.4);
}
div[data-testid="stMetric"] label {
    color: #8bafc7 !important;
    font-size: 0.78rem !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
div[data-testid="stMetricValue"] {
    color: #00d4ff !important;
    font-size: 1.9rem !important;
    font-weight: 700 !important;
}
div[data-testid="stMetricDelta"] {
    color: #8bafc7 !important;
}

/* Style Streamlit buttons */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%) !important;
    border: none !important;
    color: #0a0f1e !important;
    font-weight: 700 !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #00e5ff 0%, #00b8e6 100%) !important;
    box-shadow: 0 4px 20px rgba(0,212,255,0.35) !important;
    transform: translateY(-1px) !important;
}

/* Style file uploader */
[data-testid="stFileUploader"] {
    border: 2px dashed #1a3a5c;
    border-radius: 14px;
    padding: 1rem;
    transition: border-color 0.2s ease;
}
[data-testid="stFileUploader"]:hover {
    border-color: #00d4ff;
}

/* Style dataframes */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* Style selectbox / sliders labels */
label[data-testid="stWidgetLabel"] p {
    color: #8bafc7 !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
}

/* Style code blocks */
.stCode {
    border-radius: 10px !important;
    border: 1px solid #1a3a5c !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0a0f1e; }
::-webkit-scrollbar-thumb { background: #1a3a5c; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #00d4ff; }

</style>
"""


def card(content_html: str, extra_class: str = "") -> str:
    """Wrap content in a styled card div."""
    return f'<div class="aq-card {extra_class}">{content_html}</div>'


def metric_card(value: str, label: str, sub: str = "") -> str:
    """Return HTML for a styled metric card."""
    sub_html = f'<p class="aq-metric-sub">{sub}</p>' if sub else ""
    return f"""
    <div class="aq-metric">
        <p class="aq-metric-label">{label}</p>
        <p class="aq-metric-value">{value}</p>
        {sub_html}
    </div>"""


def section_title(title: str, subtitle: str = "") -> str:
    sub_html = f'<p class="aq-section-subtitle">{subtitle}</p>' if subtitle else ""
    return f'<h2 class="aq-section-title">{title}</h2>{sub_html}'


def divider() -> str:
    return '<hr class="aq-divider">'


def footer() -> str:
    return (
        '<div class="aq-footer">'
        'AquaGuard AI &nbsp;·&nbsp; IBM SkillsBuild ML &amp; Applied AI Internship '
        '&nbsp;·&nbsp; SDG 6 — Clean Water and Sanitation'
        '</div>'
    )


def disclaimer_bar() -> str:
    return (
        '<div class="aq-disclaimer">'
        '<strong>Disclaimer:</strong> All predictions are preliminary ML-based screening '
        'results only. They <strong>cannot certify</strong> that water is safe to drink. '
        'Always consult a certified laboratory and local health authorities.'
        '</div>'
    )
