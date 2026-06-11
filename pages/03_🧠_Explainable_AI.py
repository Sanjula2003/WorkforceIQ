import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.feature_engineering import create_workforce_health_score
from utils.model_loader import load_model

st.set_page_config(
    page_title="Explainable AI",
    layout="wide"
)

st.sidebar.title("🚀 WorkforceIQ")

st.title("🧠 Explainable AI")

st.caption(
    "Transform attrition predictions into actionable workforce insights with transparent and interpretable AI."
)

# Load data

df = load_data()
df = create_workforce_health_score(df)

model = load_model()

# Employee selector

employee_id = st.selectbox(
    "Select Employee",
    df.index
)

employee = df.iloc[[employee_id]]

# Predict risk

employee_input = employee.copy()

employee_input = employee_input.drop(
    columns=["Attrition"]
)

risk_score = (
    model.predict_proba(employee_input)[0][1]
)

# Risk level

if risk_score < 0.30:
    risk_level = "🟢 Low"

elif risk_score < 0.60:
    risk_level = "🟡 Medium"

else:
    risk_level = "🔴 High"

col1, col2 = st.columns(2)

col1.metric(
    "Attrition Risk",
    f"{risk_score:.1%}"
)

col2.metric(
    "Risk Level",
    risk_level
)

st.subheader("📌 Key Risk Factors")

factors = []

if employee["OverTime"].iloc[0] == "Yes":
    factors.append(
        "🔴 Employee is working overtime."
    )

if employee["WorkforceHealthScore"].iloc[0] < 65:
    factors.append(
        "🔴 Workforce Health Score is below average."
    )

if employee["StockOptionLevel"].iloc[0] == 0:
    factors.append(
        "🔴 Employee has no stock options."
    )

if employee["YearsWithCurrManager"].iloc[0] < 2:
    factors.append(
        "🔴 Limited time with current manager."
    )

if employee["BusinessTravel"].iloc[0] == "Travel_Frequently":
    factors.append(
        "🔴 Frequent business travel."
    )

if factors:

    for factor in factors:
        st.write(factor)

else:

    st.success(
        "No major workforce risk factors detected."
    )

st.subheader("💡 Retention Recommendations")

recommendations = []

if employee["OverTime"].iloc[0] == "Yes":
    recommendations.append(
        "Review workload and overtime allocation."
    )

if employee["WorkforceHealthScore"].iloc[0] < 65:
    recommendations.append(
        "Improve engagement and work-life balance."
    )

if employee["StockOptionLevel"].iloc[0] == 0:
    recommendations.append(
        "Evaluate retention incentives."
    )

if employee["YearsWithCurrManager"].iloc[0] < 2:
    recommendations.append(
        "Schedule manager check-ins."
    )

for rec in recommendations:
    st.success(rec)

st.subheader("👤 Employee Profile")

st.dataframe(
    employee.T,
    use_container_width=True
)

st.markdown("---")

st.caption(
    "WorkforceIQ v1.0 | AI-Powered Workforce Intelligence Platform"
)