import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.feature_engineering import create_workforce_health_score

st.title("🤖 HR Analytics Copilot")

st.caption(
    "AI-powered decision support for workforce analytics, retention strategy, and organizational risk assessment."
)

df = load_data()
df = create_workforce_health_score(df)

question = st.selectbox(
    "Ask a question",
    [
        "Which department has highest attrition?",
        "Which department has lowest workforce health?",
        "What are the top attrition drivers?",
        "How healthy is the workforce?"
    ]
)

if question == "Which department has highest attrition?":

    dept_attrition = (
        df.groupby("Department")["Attrition"]
          .apply(lambda x: (x == "Yes").mean() * 100)
          .sort_values(ascending=False)
    )

    top_dept = dept_attrition.index[0]
    rate = dept_attrition.iloc[0]

    st.success(
        f"{top_dept} has the highest attrition rate ({rate:.1f}%)."
    )

elif question == "Which department has lowest workforce health?":

    dept_health = (
        df.groupby("Department")["WorkforceHealthScore"]
          .mean()
          .sort_values()
    )

    dept = dept_health.index[0]
    score = dept_health.iloc[0]

    st.warning(
        f"{dept} has the lowest Workforce Health Score ({score:.1f})."
    )

elif question == "What are the top attrition drivers?":

    st.info(
        """
        Top Attrition Drivers:

        • Overtime

        • Job Level

        • Stock Option Level

        • Workforce Health Score

        • Years With Current Manager
        """
    )

elif question == "How healthy is the workforce?":

    score = (
        df["WorkforceHealthScore"]
        .mean()
    )

    st.success(
        f"Average Workforce Health Score: {score:.1f}/100"
    )

st.markdown("---")

st.caption(
    "WorkforceIQ | AI-Powered Workforce Intelligence Platform"
)

