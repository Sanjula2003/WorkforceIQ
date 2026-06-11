import streamlit as st
import pandas as pd

from utils.model_loader import load_model

st.set_page_config(layout="wide")

st.sidebar.title("🚀 WorkforceIQ")

st.title("🎯 Attrition Prediction")

st.caption(
    "Predict employee attrition risk using machine learning."
)

# Load data
df = pd.read_csv(
    "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Load model
model = load_model()

# Employee selector

employee_id = st.selectbox(
    "Select Employee",
    df.index
)

employee = df.iloc[[employee_id]]

if st.button("Predict Attrition Risk"):
    employee_input = employee.copy()

    employee_input["WorkforceHealthScore"] = (
        employee_input["JobSatisfaction"]
        + employee_input["WorkLifeBalance"]
        + employee_input["EnvironmentSatisfaction"]
        + employee_input["JobInvolvement"]
    ) / 16 * 100

    employee_input = employee_input.drop(
        columns=["Attrition"]
    )

    risk_score = (
        model.predict_proba(employee_input)[0][1]
    )

    if risk_score < 0.30:
        risk_level = "🟢 Low"

    elif risk_score < 0.60:
        risk_level = "🟡 Medium"

    else:
        risk_level = "🔴 High"

    col1, col2 = st.columns(2)

    col1.metric(
        "Risk Score",
        f"{risk_score:.1%}"
    )

    col2.metric(
        "Risk Level",
        risk_level
    )

st.subheader(
    "Employee Profile"
)

st.dataframe(employee.T)

st.markdown("---")

st.caption(
    "WorkforceIQ v1.0 | AI-Powered Workforce Intelligence Platform"
)