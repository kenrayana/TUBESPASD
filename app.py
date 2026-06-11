import streamlit as st
from predict import PredictaMind

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="MindFlow",
    page_icon="🧠",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("🧠 MindFlow")
st.caption("AI-Powered Mental Wellness Dashboard")

st.divider()

# =========================
# USER INPUT
# =========================

st.subheader("📋 Student Check-In")

col1, col2 = st.columns(2)

with col1:

    sleep_quality = st.slider(
        "😴 Sleep Quality",
        min_value=1,
        max_value=10,
        value=5
    )

    academic_performance = st.slider(
        "📚 Academic Performance",
        min_value=1,
        max_value=10,
        value=5
    )

with col2:

    study_load = st.slider(
        "📝 Study Load",
        min_value=1,
        max_value=10,
        value=5
    )

    extracurricular_activity = st.slider(
        "🏃 Extracurricular Activity",
        min_value=1,
        max_value=10,
        value=5
    )

# =========================
# ANALYZE BUTTON
# =========================

analyze = st.button("🔍 Analyze Now")

# =========================
# ANALYSIS RESULT
# =========================

if analyze:

    user = PredictaMind(
        sleep_quality,
        academic_performance,
        study_load,
        extracurricular_activity
    )

    stress = user.prediksi_stres()

    productivity = user.prediksi_produktivitas()

    readiness = user.hitung_readiness()

    forecast = user.productivity_forecast()

    st.divider()

    # =========================
    # METRICS
    # =========================

    colA, colB, colC = st.columns(3)

    with colA:

        st.subheader("🧘 Stress Level")

        if stress == "High":
            st.error(stress)

        elif stress == "Moderate":
            st.warning(stress)

        else:
            st.success(stress)

    with colB:

        st.subheader("📈 Productivity")

        if productivity == "High":
            st.success(productivity)

        elif productivity == "Moderate":
            st.warning(productivity)

        else:
            st.error(productivity)

    with colC:

        st.subheader("⚡ Readiness")

        st.metric(
            label="Readiness Score",
            value=f"{readiness}%"
        )

        st.progress(int(readiness))

    # =========================
    # FORECAST
    # =========================

    st.divider()

    st.subheader("⏰ Productivity Forecast")

    st.info(
        f"Recommended Productive Time: {forecast}"
    )

# =========================
# FOOTER
# =========================

st.divider()

st.caption("MindFlow © 2026")