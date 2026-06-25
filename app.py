import streamlit as st
import pandas as pd

from predict import PredictaMind

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="MindFlow",
    page_icon="🧠",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background-color:#F3F3F3;
}

/* Readiness */
.readiness-card{
    background:linear-gradient(135deg,#5B8CFF,#76A8FF);
    padding:35px;
    border-radius:25px;
    color:white;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,0.12);
}

/* Card */
.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    text-align:center;
}

/* Forecast */
.forecast-card{
    background:white;
    color:black;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.08);
    text-align:center;
}

/* Insight */
.insight-card{
    background:#ffffff;
    color:#111111;
    padding:25px;
    border-radius:20px;
    border-left:8px solid #4F8CFF;
    box-shadow:0px 3px 12px rgba(0,0,0,0.08);
}
html, body, [class*="css"]  {
    color: #111111;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: #111111 !important;
}

.input-card{
    background:white;
    border:1px solid #DCE3F0;
    border-radius:15px;
    padding:20px;
    margin-bottom:20px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.05);
}
            
.stButton > button{
    background:#2563eb !important;
    color:white !important;
    border:none !important;
    border-radius:12px !important;
    height:55px !important;
    font-size:18px !important;
    font-weight:600 !important;
}

.stButton > button:hover{
    background:#1d4ed8 !important;
    transform:translateY(-2px);
}
</style>
""", unsafe_allow_html=True)



# ==================================
# HEADER
# ==================================

st.title("MindFlow")

st.markdown("""
### Hi, Raya! 👋

Ready for flow today?
""")

st.divider()

# ==================================
# STUDENT CHECK-IN
# ==================================
st.markdown("## 📋 Student Check-In")

sidebar_col, main_col = st.columns([1,5])

with sidebar_col:

    st.markdown("""
    <div class="input-card">
        <h4>How it works</h4>

        1. Fill your data
        Answer each section based on your current condition.<br><br>

        2. Get insights
        AI analyzes your input and generates a dashboard.<br><br>

        3. Improve your day
        Use recommendations to make better decisions.<br><br>

        <hr>

        🔒 Your data is private
    </div>
    """,
    unsafe_allow_html=True)

# ==========================
# LEFT COLUMN
# ==========================
with main_col:

    input_col1, input_col2 = st.columns(2)

    with input_col1:

        st.markdown('<div class="input-card">', unsafe_allow_html=True)

        sleep_quality = st.radio(
            "😴 Sleep Quality",
            options=list(range(1,11)),
            horizontal=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="input-card">', unsafe_allow_html=True)

        academic_performance = st.radio(
            "📚 Academic Performance",
            options=list(range(1,11)),
            horizontal=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# RIGHT COLUMN
# ==========================

    with input_col2:

        st.markdown('<div class="input-card">', unsafe_allow_html=True)

        study_load_text = st.radio(
            "📚 Study Load",
            ["Light","Medium","Heavy"],
            horizontal=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="input-card">', unsafe_allow_html=True)

        extracurricular_activity = st.radio(
            "🏃 Extracurricular Activity",
            options=list(range(1,11)),
            horizontal=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

   
# ==========================
# CONVERT STUDY LOAD
# ==========================

if study_load_text == "Light":
    study_load = 3
elif study_load_text == "Medium":
    study_load = 6
else:
    study_load = 9

st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button(
    "🚀 Submit Check-In",
    use_container_width=True
)

st.divider()

# ==================================
# ANALYSIS
# ==================================

if analyze:

    user = PredictaMind(
        sleep_quality,
        academic_performance,
        study_load,
        extracurricular_activity
    )

    # ==========================
    # PREDICTION
    # ==========================

    stress = user.prediksi_stres()

    productivity = user.prediksi_produktivitas()

    readiness = user.hitung_readiness()

    forecast = user.productivity_forecast()

    # ==========================
    # TREND
    # ==========================

    if stress == "High":
        trend = "Increasing"

    elif stress == "Moderate":
        trend = "Stable"

    else:
        trend = "Decreasing"

    # ==========================
    # PRODUCTIVITY CHART
    # ==========================

    chart_data = pd.DataFrame(
        {
            "Productivity": [40, 75, 100, 80, 50]
        },
        index=["AM", "10AM", "NOON", "3PM", "PM"]
    )

    # ==================================
    # DAILY READINESS
    # ==================================

    energy = "High"
    if readiness < 60:
        energy = "Low"
    elif readiness < 80:
        energy = "Medium"
    st.markdown(
        f"""
        <div class="readiness-card">
          <h3>⚡ Daily Readiness</h3>
          <h1 style="font-size:72px;">{readiness}%</h1>
          <h4>Energy Level: {energy}</h4>
        </div>
        """,
        unsafe_allow_html=True
        )


    # ==================================
    # STATUS SECTION
    # ==================================

    colA, colB = st.columns(2)
    with colA:
        st.markdown(
            f"""
            <div class="card">
            <h3>🧘 Current Status</h3>
            <h2>{stress}</h2>
            <p>Trend: {trend}</p>
        </div>
        """,
        unsafe_allow_html=True
        )
    with colB:

        st.markdown(
            f"""
            <div class="card">
            <h3>📈 Productivity</h3>
            <h2>{productivity}</h2>
        </div>
        """,
        unsafe_allow_html=True
        )
    st.divider()
    # ==================================
    # PRODUCTIVITY FORECAST
    # ==================================

    col1, col2 = st.columns(2)
    with col1:
        
        st.markdown(
            f"""
            <div class="forecast-card">
            <h3>⏰ Productivity Forecast</h3>
            <h1>{forecast}</h1>
            <p>Your recommended productive period.</p>
        </div>
        """,
        unsafe_allow_html=True
        )

    with col2:

        st.subheader("📊 Forecast Pattern")
        st.bar_chart(chart_data)
    st.divider()

    # ==================================
    # AI INSIGHT
    # ==================================

    st.subheader("💡 AI Insight")

    if stress == "High":

        insight = """
        Your stress level is high.<br>
        • Improve sleep quality<br>
        • Reduce study overload<br>
        • Take short breaks between study sessions
        """

    elif stress == "Moderate":

        insight = """
        Your condition is relatively balanced.<br>
        • Maintain study-rest balance<br>
        • Keep a consistent sleep schedule<br>
        • Avoid excessive workload
        """

    else:

        insight = """
        Excellent condition!<br>
        • Continue your current habits<br>
        • Utilize your productive hours effectively<br>
        • Maintain healthy routines
        """

    st.markdown(
        f"""
        <div class="insight-card">
            {insight}
        </div>
        """,
        unsafe_allow_html=True
    )

# ==================================
# FOOTER
# ==================================

st.divider()

st.caption("MindFlow © 2026")