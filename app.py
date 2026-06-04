import streamlit as st
from predict import PredictaMind

# KONFIGURASI PAGE


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
# QUICK CHECK-IN
# =========================

st.subheader("📋 Quick Check-In")

col1, col2, col3 = st.columns(3)

with col1:
    jam_tidur = st.number_input(
        "Jam Tidur",
        min_value=0,
        max_value=24,
        value=7
    )

with col2:
    aktivitas = st.slider(
        "Aktivitas Harian",
        1,
        10,
        value=5
    )

with col3:
    mood = st.slider(
        "Mood Harian",
        1,
        10,
        value=7
    )

# =========================
# BUTTON
# =========================

analyze = st.button("🔍 Analyze Now")

# =========================
# HASIL ANALISIS
# =========================

if analyze:

    # Membuat object
    user = PredictaMind(
        jam_tidur,
        aktivitas,
        mood
    )

    # =========================
    # MEMANGGIL METHOD
    # =========================

    stress_score = user.prediksi_stres()

    kategori_stres = user.kategori_stres()

    produktivitas = user.prediksi_produktivitas()

    readiness = user.hitung_readiness()

    forecast = user.productivity_forecast()

    # =========================
    # DASHBOARD SECTION
    # =========================

    st.divider()

    colA, colB = st.columns(2)

    # =========================
    # DAILY READINESS
    # =========================

    with colA:

        st.subheader("⚡ Daily Readiness")

        st.metric(
            label="Readiness Score",
            value=f"{readiness}%"
        )

        st.progress(int(readiness))

        if readiness >= 80:
            st.success("Energy Level: High")

        elif readiness >= 60:
            st.warning("Energy Level: Medium")

        else:
            st.error("Energy Level: Low")

    # =========================
    # STRESS METER
    # =========================

    with colB:

        st.subheader("🧘 Stress Meter")

        st.progress(int(stress_score))

        st.metric(
            label="Stress Score",
            value=f"{stress_score}%"
        )

        st.write(f"Stress Level: **{kategori_stres}**")

    # =========================
    # PRODUKTIVITAS
    # =========================

    st.divider()

    st.subheader("📈 Productivity Forecast")

    colC, colD = st.columns(2)

    with colC:

        st.info(
            f"Produktivitas Hari Ini: {produktivitas}"
        )

    with colD:

        st.success(
            f"Optimal Productivity Time: {forecast}"
        )

# =========================
# FOOTER
# =========================

st.divider()

st.caption("MindFlow © 2026")