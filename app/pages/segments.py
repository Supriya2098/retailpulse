
import streamlit as st

import pandas as pd

import numpy as np

import plotly.express as px

from sklearn.decomposition import PCA

# ============================================================
# LOAD MOCK SEGMENT DATA
# ============================================================

def load_segments():

    np.random.seed(42)

    n = 300

    df = pd.DataFrame({

        "Recency": np.random.randint(1, 200, n),

        "Frequency": np.random.randint(1, 50, n),

        "Monetary": np.random.randint(100, 5000, n),

        "Segment": np.random.choice([

            "Champions",

            "Loyal",

            "At Risk",

            "Potential",

            "Hibernating",

            "New"

        ], n)

    })

    return df

# ============================================================
# PAGE
# ============================================================

def render():

    st.title(

        "👥 Customer Segmentation"

    )

    df = load_segments()

    # ========================================================
    # PCA
    # ========================================================

    features = df[[

        "Recency",

        "Frequency",

        "Monetary"

    ]]

    pca = PCA(n_components=2)

    comps = pca.fit_transform(features)

    df["PCA1"] = comps[:, 0]

    df["PCA2"] = comps[:, 1]

    # ========================================================
    # PLOT
    # ========================================================

    fig = px.scatter(

        df,

        x="PCA1",

        y="PCA2",

        color="Segment",

        title="Customer Segments (PCA Projection)",

        hover_data=[

            "Recency",

            "Frequency",

            "Monetary"

        ]

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ========================================================
    # KPI TABLE
    # ========================================================

    st.subheader(

        "📊 Segment KPI Summary"

    )

    summary = df.groupby(

        "Segment"

    ).agg({

        "Recency": "mean",

        "Frequency": "mean",

        "Monetary": "mean"

    }).round(2)

    st.dataframe(

        summary,

        use_container_width=True

    )
