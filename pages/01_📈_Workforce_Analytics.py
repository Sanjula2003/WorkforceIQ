import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.sidebar.title("🚀 WorkforceIQ")

# Load data
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Workforce Health Score
df["WorkforceHealthScore"] = (
    df["JobSatisfaction"]
    + df["WorkLifeBalance"]
    + df["EnvironmentSatisfaction"]
    + df["JobInvolvement"]
) / 16 * 100

# Attrition Flag
df["AttritionFlag"] = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})

st.title("📈 Workforce Analytics")

st.caption(
    "Analyze workforce health, attrition trends, and organizational risk."
)

# Executive KPIs

total_employees = len(df)

attrition_rate = (
    (df["Attrition"] == "Yes").mean()
) * 100

avg_health = (
    df["WorkforceHealthScore"]
    .mean()
)

avg_salary = (
    df["MonthlyIncome"]
    .mean()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Employees",
    f"{total_employees:,}"
)

col2.metric(
    "Attrition Rate",
    f"{attrition_rate:.1f}%"
)

col3.metric(
    "Workforce Health",
    f"{avg_health:.1f}"
)

col4.metric(
    "Avg Salary",
    f"${avg_salary:,.0f}"
)


# Department workforce analysis

dept_health = (
    df.groupby("Department")
      .agg({
          "WorkforceHealthScore": "mean",
          "AttritionFlag": "mean"
      })
      .reset_index()
)

dept_health["AttritionFlag"] *= 100

left, right = st.columns(2)

# Workforce health distribution

fig_health = px.histogram(
    df,
    x="WorkforceHealthScore",
    nbins=20,
    title="Workforce Health Distribution"
)

left.plotly_chart(
    fig_health,
    use_container_width=True
)

# Department risk matrix

fig_risk = px.scatter(
    dept_health,
    x="WorkforceHealthScore",
    y="AttritionFlag",
    size="AttritionFlag",
    color="Department",
    text="Department",
    title="Department Risk Matrix"
)

right.plotly_chart(
    fig_risk,
    use_container_width=True
)


# Executive insights

st.markdown("---")

st.subheader("📌 Executive Insights")

highest_risk_dept = (
    dept_health
    .sort_values(
        "AttritionFlag",
        ascending=False
    )
    .iloc[0]
)

st.info(
    f"""
    Sales has the highest attrition rate
    ({highest_risk_dept['AttritionFlag']:.1f}%).

    This department should be prioritized
    for retention initiatives.
    """
)

overtime_risk = (
    pd.crosstab(
        df["OverTime"],
        df["Attrition"],
        normalize="index"
    ) * 100
)

risk_multiplier = (
    overtime_risk.loc["Yes", "Yes"]
    /
    overtime_risk.loc["No", "Yes"]
)

st.warning(
    f"""
    Employees working overtime are
    {risk_multiplier:.1f}x more likely
    to leave the organization.
    """
)

st.markdown("---")

st.caption(
    "WorkforceIQ v1.0 | AI-Powered Workforce Intelligence Platform"
)