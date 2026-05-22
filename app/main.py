
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
# PAGE ROUTING
# ============================================================

if page.startswith("🏠"):

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
    """)

    st.divider()

    # ========================================================
    # KPI STRIP
    # ========================================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Hybrid Forecast MAPE",
        "4.61%"
    )

    col2.metric(
        "Churn Model AUC",
        "0.94"
    )

    col3.metric(
        "Projected Stockout Reduction",
        "32.7%"
    )

    st.divider()

    # ========================================================
    # PROJECT SUMMARY
    # ========================================================

    st.subheader(
        "📊 System Overview"
    )

    st.markdown("""

    RetailPulse is an end-to-end AI-powered retail analytics platform designed for:

    - Demand Forecasting
    - Customer Intelligence
    - Churn Prediction
    - Inventory Optimization
    - Model Monitoring
    - Automated ML Retraining

    ### Tech Stack

    - Streamlit
    - Prophet
    - PyTorch Lightning
    - XGBoost
    - MLflow
    - Evidently AI
    - Docker + Kubernetes

    """)

# ============================================================
# FORECASTING PAGE
# ============================================================

elif page.startswith("📈"):

    from app.pages import forecasting as p

    p.render()

# ============================================================
# SEGMENTS PAGE
# ============================================================

elif page.startswith("👥"):

    from app.pages import segments as p

    p.render()

# ============================================================
# CHURN PAGE
# ============================================================

elif page.startswith("⚠️"):

    from app.pages import churn as p

    p.render()

# ============================================================
# INVENTORY PAGE
# ============================================================

elif page.startswith("📦"):

    from app.pages import inventory as p

    p.render()

# ============================================================
# MONITORING PAGE
# ============================================================

else:

    from app.pages import monitoring as p

    p.render()
