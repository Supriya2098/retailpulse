
import streamlit as st


st.set_page_config(

    page_title="RetailPulse Analytics",

    page_icon="🛒",

    layout="wide",

    initial_sidebar_state="expanded"

)


st.sidebar.title(

    "🛒 RetailPulse"

)

st.sidebar.caption(

    "AI-Powered Retail Analytics Platform"

)

st.sidebar.markdown("---")


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


elif page == "📈 Demand Forecasting":

    import pages.forecasting as p

    p.render()


elif page == "👥 Customer Segments":

    import pages.segments as p

    p.render()


elif page == "⚠️ Churn Risk":

    import pages.churn as p

    p.render()



elif page == "📦 Inventory Optimizer":

    import pages.inventory as p

    p.render()


elif page == "🔬 Model Monitoring":

    import pages.monitoring as p

    p.render()
