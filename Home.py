import streamlit as st

st.set_page_config(
    page_title="WorkforceIQ",
    page_icon="📊",
    layout="wide"
)

st.title("📊 WorkforceIQ")

st.subheader(
    "Predict • Explain • Retain"
)

st.caption(
    "AI-powered HR analytics platform for workforce intelligence and employee retention."
)

st.markdown("---")

st.markdown("""
### Features

✅ Workforce Analytics

✅ Attrition Prediction

✅ Explainable AI

✅ Workforce Health Score

✅ AI HR Assistant

---
            


Built using:

- XGBoost
- SHAP
- Streamlit
- Plotly
- HR Analytics
""")


st.markdown("---")

st.subheader("🎯 Business Problem")

st.write(
    """
    Employee attrition results in recruitment costs,
    productivity loss, and workforce instability.

    WorkforceIQ helps HR leaders proactively identify
    retention risks using predictive analytics,
    explainable AI, and workforce intelligence.
    """
)

st.markdown("---")

st.metric(
    "Model ROC-AUC",
    "0.78"
)

st.metric(
    "Employees Analyzed",
    "1,470"
)

st.markdown("---")

st.caption(
    "WorkforceIQ | AI-Powered Workforce Intelligence Platform"
)