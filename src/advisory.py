"""
advisory.py
-----------
WHO-based threshold checks, risk-tier classification, and plain-English advice.
"""

from dataclasses import dataclass, field
from typing import Optional

# ---------------------------------------------------------------------------
# WHO / standard guideline thresholds
# ---------------------------------------------------------------------------
WHO_THRESHOLDS: dict[str, dict] = {
    "ph": {
        "label": "pH",
        "unit": "",
        "safe_min": 6.5,
        "safe_max": 8.5,
        "description": "Measures acidity/alkalinity of water.",
        "low_advice":  "pH is too low (acidic). Acidic water can leach metals from pipes.",
        "high_advice": "pH is too high (alkaline). May cause scale build-up and bitter taste.",
    },
    "Hardness": {
        "label": "Hardness",
        "unit": "mg/L",
        "safe_min": 0,
        "safe_max": 300,
        "description": "Caused by dissolved calcium and magnesium salts.",
        "low_advice":  None,
        "high_advice": "Very hard water may cause scale and reduce soap effectiveness.",
    },
    "Solids": {
        "label": "Total Dissolved Solids (TDS)",
        "unit": "ppm",
        "safe_min": 0,
        "safe_max": 500,
        "description": "Total dissolved inorganic/organic substances.",
        "low_advice":  None,
        "high_advice": "High TDS can indicate contamination and affects taste.",
    },
    "Chloramines": {
        "label": "Chloramines",
        "unit": "ppm",
        "safe_min": 0,
        "safe_max": 4,
        "description": "Disinfectants formed when chlorine reacts with ammonia.",
        "low_advice":  None,
        "high_advice": "Excessive chloramines can cause health issues over long-term exposure.",
    },
    "Sulfate": {
        "label": "Sulfate",
        "unit": "mg/L",
        "safe_min": 0,
        "safe_max": 250,
        "description": "Naturally occurring mineral found in water.",
        "low_advice":  None,
        "high_advice": "High sulfate may cause a laxative effect and bitter taste.",
    },
    "Conductivity": {
        "label": "Conductivity",
        "unit": "μS/cm",
        "safe_min": 0,
        "safe_max": 400,
        "description": "Electrical conductivity indicates dissolved ion concentration.",
        "low_advice":  None,
        "high_advice": "High conductivity may indicate excessive dissolved minerals or contamination.",
    },
    "Organic_carbon": {
        "label": "Organic Carbon",
        "unit": "ppm",
        "safe_min": 0,
        "safe_max": 2,
        "description": "Measure of total organic compounds in water.",
        "low_advice":  None,
        "high_advice": "High organic carbon can promote microbial growth and form disinfection by-products.",
    },
    "Trihalomethanes": {
        "label": "Trihalomethanes (THMs)",
        "unit": "μg/L",
        "safe_min": 0,
        "safe_max": 80,
        "description": "By-products formed during chlorination of water.",
        "low_advice":  None,
        "high_advice": "THMs above guideline levels are associated with increased cancer risk.",
    },
    "Turbidity": {
        "label": "Turbidity",
        "unit": "NTU",
        "safe_min": 0,
        "safe_max": 5,
        "description": "Cloudiness caused by suspended particles.",
        "low_advice":  None,
        "high_advice": "High turbidity can indicate pathogens and reduces disinfection effectiveness.",
    },
}

# ---------------------------------------------------------------------------
# Risk tier thresholds (based on model probability of potable)
# ---------------------------------------------------------------------------
TIER_HIGH    = 0.35   # probability < TIER_HIGH → High Risk
TIER_MODERATE = 0.65  # TIER_HIGH ≤ prob < TIER_MODERATE → Moderate Risk
                      # prob ≥ TIER_MODERATE → Low Risk


@dataclass
class AdvisoryResult:
    risk_tier: str                          # "High Risk" | "Moderate Risk" | "Low Risk"
    tier_color: str                         # "red" | "orange" | "green"
    tier_emoji: str
    probability_potable: float
    violations: list[dict] = field(default_factory=list)
    next_steps: list[str]  = field(default_factory=list)


def classify_risk_tier(prob_potable: float) -> tuple[str, str, str]:
    if prob_potable < TIER_HIGH:
        return "High Risk", "red", "🔴"
    elif prob_potable < TIER_MODERATE:
        return "Moderate Risk", "orange", "🟡"
    else:
        return "Low Risk", "green", "🟢"


def check_who_violations(values: dict) -> list[dict]:
    """Return list of threshold violations for a sample dict."""
    violations = []
    for feature, thresholds in WHO_THRESHOLDS.items():
        val = values.get(feature)
        if val is None:
            continue
        lo = thresholds["safe_min"]
        hi = thresholds["safe_max"]
        if lo is not None and val < lo:
            violations.append({
                "feature": feature,
                "label": thresholds["label"],
                "value": val,
                "unit": thresholds["unit"],
                "advice": thresholds["low_advice"],
                "direction": "below",
                "limit": lo,
            })
        elif hi is not None and val > hi:
            violations.append({
                "feature": feature,
                "label": thresholds["label"],
                "value": val,
                "unit": thresholds["unit"],
                "advice": thresholds["high_advice"],
                "direction": "above",
                "limit": hi,
            })
    return violations


def build_next_steps(tier: str, violations: list[dict]) -> list[str]:
    steps = []
    if tier == "High Risk":
        steps.append("Do NOT use this water for drinking or cooking without treatment.")
        steps.append("Contact your local water authority or environmental health department immediately.")
        steps.append("Arrange professional laboratory testing as soon as possible.")
    elif tier == "Moderate Risk":
        steps.append("Exercise caution — this water requires further verification before use.")
        steps.append("Boil water before drinking if no other safe source is available.")
        steps.append("Consider professional water testing to confirm safety.")
    else:
        steps.append("Preliminary screening suggests lower risk, but always verify with official testing.")

    if any(v["feature"] == "Turbidity" for v in violations):
        steps.append("Use a filtration system or allow water to settle before any treatment.")
    if any(v["feature"] == "Trihalomethanes" for v in violations):
        steps.append("Allow water to stand open for 30 minutes or use activated carbon filtration to reduce THMs.")
    if any(v["feature"] in ("ph",) for v in violations):
        steps.append("Use pH-neutralising filters appropriate for your water source.")

    steps.append(
        "⚠️ DISCLAIMER: These are preliminary ML-based screening results only. "
        "They cannot certify that water is safe to drink. Always consult a certified "
        "laboratory and local health authorities for definitive water safety assessment."
    )
    return steps


def get_advisory(prob_potable: float, values: dict) -> AdvisoryResult:
    tier, color, emoji = classify_risk_tier(prob_potable)
    violations = check_who_violations(values)
    next_steps = build_next_steps(tier, violations)
    return AdvisoryResult(
        risk_tier=tier,
        tier_color=color,
        tier_emoji=emoji,
        probability_potable=prob_potable,
        violations=violations,
        next_steps=next_steps,
    )
