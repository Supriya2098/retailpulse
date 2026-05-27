
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
<<<<<<< HEAD

    "🛒 RetailPulse"

)

st.sidebar.caption(

    "AI-Powered Retail Analytics Platform"

=======
    "🛒 RetailPulse"
)

st.sidebar.caption(
    "AI-Powered Retail Analytics Platform"
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e
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
<<<<<<< HEAD
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

=======
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
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e
    ### Platform Features

    - 📈 Hybrid Demand Forecasting
    - 👥 Customer Segmentation
    - ⚠️ Churn Prediction
    - 📦 Inventory Optimization
    - 🔬 Drift Monitoring
    - 🤖 Automated Retraining
    - ☁️ Cloud Deployment
<<<<<<< HEAD
    - 📊 Prometheus + Grafana Monitoring

=======
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e
    """)

    st.divider()

    # ========================================================
    # KPI STRIP
    # ========================================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
<<<<<<< HEAD

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

=======
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
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e
    )

    st.divider()

    # ========================================================
    # PROJECT SUMMARY
    # ========================================================

    st.subheader(
<<<<<<< HEAD

        "📊 System Overview"

=======
        "📊 System Overview"
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e
    )

    st.markdown("""

<<<<<<< HEAD
    RetailPulse is an end-to-end AI-powered retail analytics platform built for:

    - Demand Forecasting
    - Customer Segmentation
    - Churn Prediction
    - Inventory Optimization
    - Real-Time Monitoring
=======
    RetailPulse is an end-to-end AI-powered retail analytics platform designed for:

    - Demand Forecasting
    - Customer Intelligence
    - Churn Prediction
    - Inventory Optimization
    - Model Monitoring
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e
    - Automated ML Retraining

    ### Tech Stack

    - Streamlit
    - Prophet
    - PyTorch Lightning
    - XGBoost
    - MLflow
    - Evidently AI
<<<<<<< HEAD
    - Docker
    - Kubernetes
    - Prometheus
    - Grafana
=======
    - Docker + Kubernetes
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e

    """)

# ============================================================
# FORECASTING PAGE
# ============================================================

<<<<<<< HEAD
elif page == "📈 Demand Forecasting":

    import app.pages.forecasting as p
=======
elif page.startswith("📈"):

    from app.pages import forecasting as p
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e

    p.render()

# ============================================================
# SEGMENTS PAGE
# ============================================================

<<<<<<< HEAD
elif page == "👥 Customer Segments":

    import app.pages.segments as p
=======
elif page.startswith("👥"):

    from app.pages import segments as p
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e

    p.render()

# ============================================================
# CHURN PAGE
# ============================================================

<<<<<<< HEAD
elif page == "⚠️ Churn Risk":

    import app.pages.churn as p
=======
elif page.startswith("⚠️"):

    from app.pages import churn as p
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e

    p.render()

# ============================================================
# INVENTORY PAGE
# ============================================================

<<<<<<< HEAD
elif page == "📦 Inventory Optimizer":

    import app.pages.inventory as p
=======
elif page.startswith("📦"):

    from app.pages import inventory as p
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e

    p.render()

# ============================================================
# MONITORING PAGE
# ============================================================

<<<<<<< HEAD
elif page == "🔬 Model Monitoring":

    import app.pages.monitoring as p
=======
else:

    from app.pages import monitoring as p
>>>>>>> 9044d63e0b9bfb19ca3fa308c0ca1e1e3ef63b4e

    p.render()
