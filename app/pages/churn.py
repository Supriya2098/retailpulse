
import streamlit as st

import pandas as pd

import numpy as np

# ============================================================
# LOAD MOCK CHURN DATA
# ============================================================

def load_churn():

    np.random.seed(42)

    customers = []

    reasons = [

        "High Recency",

        "Low Frequency",

        "No Recent Orders",

        "Low Spend",

        "Declining Activity"

    ]

    for i in range(1, 21):

        customers.append({

            "CustomerID": f"CUST{i:04d}",

            "ChurnProbability": round(

                np.random.uniform(0.70, 0.99),

                2

            ),

            "TopReason1": np.random.choice(reasons),

            "TopReason2": np.random.choice(reasons),

            "TopReason3": np.random.choice(reasons)

        })

    return pd.DataFrame(customers)

# ============================================================
# PAGE
# ============================================================

def render():

    st.title(

        "⚠️ Churn Risk Dashboard"

    )

    df = load_churn()

    # ========================================================
    # TOP N
    # ========================================================

    top_n = st.slider(

        "Top At-Risk Customers",

        5,

        20,

        10

    )

    risk_df = df.sort_values(

        "ChurnProbability",

        ascending=False

    ).head(top_n)

    # ========================================================
    # TABLE
    # ========================================================

    st.subheader(

        "🚨 High-Risk Customers"

    )

    st.dataframe(

        risk_df,

        use_container_width=True

    )

    # ========================================================
    # METRICS
    # ========================================================

    avg_risk = risk_df[

        "ChurnProbability"

    ].mean()

    st.metric(

        "Average Churn Risk",

        f"{avg_risk:.2%}"

    )
