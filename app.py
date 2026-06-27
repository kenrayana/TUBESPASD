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

/* ============ GLOBAL THEME ============ */

:root {
    --bg-primary: #0B1120;
    --bg-secondary: #111827;
    --card-bg: #141B2D;

    --border-primary: #7C3AED;
    --border-secondary: #3B82F6;

    --text-primary: #FFFFFF;
    --text-secondary: #A1A7B8;
}

/* Background halaman */

[data-testid="stAppViewContainer"],
.main,
.block-container {
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
}

h1, h2, h3, h4, h5, h6,
p, label, span, div,
.stMarkdown,
.stText,
.stRadio label {
    color: var(--text-primary) !important;
}

.stCaption,
small {
    color: var(--text-secondary) !important;
}
            
/* Readiness */
.readiness-card{
    background:linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    );

    padding:35px;
    border-radius:25px;

    color:white;

    border:none;

    box-shadow:
        0 0 30px rgba(59,130,246,0.35);
}

/* Card */
.card{
    background:#131C31;
    border:1px solid #334155;
    padding:25px;
    border-radius:20px;
    color:white;
    box-shadow:
        0 4px 15px rgba(0,0,0,0.2);
}

/* Forecast */
.forecast-card{
    background:#131C31;
    color:white;
    padding:25px;
    border-radius:20px;
    border:1px solid #334155;
    box-shadow:
        0 4px 15px rgba(0,0,0,0.2);
    text-align:center;
}

/* Insight */
.insight-card{
    background:#131C31;

    color:white;

    padding:25px;

    border-radius:20px;

    border-left:8px solid #4F8CFF;

    border-top:1px solid #334155;
    border-right:1px solid #334155;
    border-bottom:1px solid #334155;

    box-shadow:
        0 4px 15px rgba(0,0,0,0.2);
}
html, body, [class*="css"]  {
    color: #F8FAFC;
}

h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF !important;
}

p, label, span {
    color: #CBD5E1 !important;
}
.input-card {
    background: var(--card-bg);

    border: 2px solid var(--border-secondary);

    border-radius: 18px;

    padding: 16px 20px;

    margin-bottom: 16px;

    box-shadow: 0 0 15px rgba(59,130,246,0.15);

    transition: all 0.3s ease;
}

.input-card:hover {
    border-color: var(--border-primary);

    box-shadow: 0 0 20px rgba(124,58,237,0.35);
}

/* Perbaikan radio horizontal agar terlihat bagus */

[data-testid="stHorizontalBlock"] {
    gap: 16px !important;
    flex-wrap: nowrap !important;
}

[data-testid="stRadio"] label {
    color: var(--text-primary) !important;
    font-weight: 500;
}

[data-testid="stRadio"] div[role="radiogroup"] {
    flex-wrap: nowrap;
    gap: 14px;
}
            
.how-card {
    background: linear-gradient(180deg, #111827, #0F172A);
    border: 2px solid var(--border-primary);
    border-radius: 18px;
    padding: 20px;

    box-shadow: 0 0 20px rgba(124, 58, 237, 0.25);

    color: var(--text-primary);

    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.how-title{
    color:white;
    font-size:18px;
    font-weight:700;
    margin-bottom:15px;
}

.num{
    width:28px;
    height:28px;

    background:#7C3AED;

    color:white;

    border-radius:8px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-weight:bold;
}

.content{
    color:#CBD5E1;
}

.privacy{
    margin-top:15px;
    padding-top:10px;
    border-top:1px solid #334155;
    color:#94A3B8;
    font-size:13px;
}


            
.stButton > button{
    width:100%;
    height:55px;

    border:none;
    border-radius:15px;

    color:white;
    font-weight:bold;
    font-size:18px;

    background:linear-gradient(
        90deg,
        #7C3AED,
        #3B82F6
    );

    box-shadow:
        0 0 15px rgba(124,58,237,0.4);

    transition:all .3s ease;
}

.stButton > button:hover{
    transform:translateY(-2px);

    box-shadow:
        0 0 25px rgba(124,58,237,0.7);

    background:linear-gradient(
        90deg,
        #8B5CF6,
        #60A5FA
    );
}

.stRadio label,
.stMarkdown,
.stText,
div {
    color:#F8FAFC !important;
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

col_sidebar, col_form = st.columns([1.1, 3.9])

# =========================
# HOW IT WORKS
# =========================
with col_sidebar:
    st.markdown("""
<div class="how-card">

<h3>💡 How it Works</h3>

<div class="step">
<strong>① Fill your data</strong><br>
Answer each question based on your current condition.
</div>

<div class="step">
<strong>② Get insights</strong><br>
AI analyzes your input and predicts your stress level.
</div>

<div class="step">
<strong>③ Improve your day</strong><br>
Receive recommendations to maintain better mental wellness.
</div>

<div class="privacy">
🔒 Your data is private
</div>

</div>
""", unsafe_allow_html=True)
# =========================
# FORM INPUT
# =========================
with col_form:

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            sleep_quality = st.radio(
                "😴 Sleep Quality",
                options=list(range(1,11)),
                horizontal=True,
                key="sleep"
            )

        with st.container(border=True):

            academic_performance = st.radio(
                "📚 Academic Performance",
                options=list(range(1,11)),
                horizontal=True,
                key="academic"
            )

    with right:

        with st.container(border=True):

            study_load_text = st.radio(
                "📚 Study Load",
                ["Light","Medium","Heavy"],
                horizontal=True,
                key="study"
            )

        with st.container(border=True):

            extracurricular_activity = st.radio(
                "🏃 Extracurricular Activity",
                options=list(range(1,11)),
                horizontal=True,
                key="extra"
            )

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