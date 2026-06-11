def create_workforce_health_score(df):

    df["WorkforceHealthScore"] = (
        df["JobSatisfaction"]
        + df["WorkLifeBalance"]
        + df["EnvironmentSatisfaction"]
        + df["JobInvolvement"]
    ) / 16 * 100

    return df