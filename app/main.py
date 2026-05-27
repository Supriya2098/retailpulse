
import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(

    page_title="RetailPulse Analytics",

    page_icon="🛒",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(

    "🛒 RetailPulse"

)

st.sidebar.caption(

    "AI-Powered Retail Analytics Platform"

)

st.sidebar.markdown("---")

# ============================================================
# NAVIGATION
# ============================================================

page = st.sidebar.radio(

    "Navigate",

    [

        "🏠 Overview",

        "📈 Demand Forecasting",

        "👥 Customer Segments",

        "⚠️ Churn Risk",

        "📦 Inventory Optimizer",

        "🔬 Model Monitoring"

    ]

)

# ============================================================
# OVERVIEW PAGE
# ============================================================

if page == "🏠 Overview":

    st.title(

        "🚀 RetailPulse Dashboard"

    )

    st.subheader(

        "AI-Powered Retail Analytics Platform"

    )

    st.markdown("""

    ### Platform Features

    - 📈 Hybrid Demand Forecasting
    - 👥 Customer Segmentation
    - ⚠️ Churn Prediction
    - 📦 Inventory Optimization
    - 🔬 Drift Monitoring
    - 🤖 Automated Retraining
    - ☁️ Cloud Deployment
    - 📊 Prometheus + Grafana Monitoring

    """)

    st.divider()

    # ========================================================
    # KPI STRIP
    # ========================================================

    col1, col2, col3 = st.columns(3)

    col1.metric(

        "Forecast MAPE",

        "10.4%"

    )

    col2.metric(

        "Churn AUC",

        "0.928"

    )

    col3.metric(

        "Stockout Reduction",

        "32%"

    )

    st.divider()

    # ========================================================
    # PROJECT SUMMARY
    # ========================================================

    st.subheader(

        "📊 System Overview"

    )

    st.markdown("""

    RetailPulse is an end-to-end AI-powered retail analytics platform built for:

    - Demand Forecasting
    - Customer Segmentation
    - Churn Prediction
    - Inventory Optimization
    - Real-Time Monitoring
    - Automated ML Retraining

    ### Tech Stack

    - Streamlit
    - Prophet
    - PyTorch Lightning
    - XGBoost
    - MLflow
    - Evidently AI
    - Docker
    - Kubernetes
    - Prometheus
    - Grafana

    """)

# ============================================================
# FORECASTING PAGE
# ============================================================

elif page == "📈 Demand Forecasting":

    import app.pages.forecasting as p

    p.render()

# ============================================================
# SEGMENTS PAGE
# ============================================================

elif page == "👥 Customer Segments":

    import app.pages.segments as p

    p.render()

# ============================================================
# CHURN PAGE
# ============================================================

elif page == "⚠️ Churn Risk":

    import app.pages.churn as p

    p.render()

# ============================================================
# INVENTORY PAGE
# ============================================================

elif page == "📦 Inventory Optimizer":

    import app.pages.inventory as p

    p.render()

# ============================================================
# MONITORING PAGE
# ============================================================

elif page == "🔬 Model Monitoring":

    import app.pages.monitoring as p

    p.render()
