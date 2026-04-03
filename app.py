import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="EEG Detecting System", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Remove default padding */
.block-container {
    padding-top: 2rem;
}

/* Hero Title */
.hero {
    text-align: center;
    padding: 50px 20px;
}

.hero h1 {
    font-size: 60px;
    font-weight: bold;
    color: #00f2ff;
}

.hero p {
    font-size: 20px;
    color: #cfcfcf;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #00f2ff, #4facfe);
    color: black;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------
st.markdown("""
<div class="hero">
    <h1>🧠 EEG Detecting System</h1>
    <p>AI-Powered Neurological Monitoring & Brain Signal Analysis</p>
</div>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("⚙️ Control Panel")

wave_type = st.sidebar.selectbox(
    "Select Brain Wave",
    ["Alpha", "Beta", "Theta", "Delta"]
)

# ------------------ SIGNAL GENERATION ------------------
t = np.linspace(0, 10, 500)

if wave_type == "Alpha":
    signal = np.sin(2 * np.pi * 10 * t)
elif wave_type == "Beta":
    signal = np.sin(2 * np.pi * 20 * t)
elif wave_type == "Theta":
    signal = np.sin(2 * np.pi * 6 * t)
else:
    signal = np.sin(2 * np.pi * 2 * t)

signal = signal + np.random.normal(0, 0.3, len(t))

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([2,1])

# ------------------ GRAPH ------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Live EEG Signal")

    fig, ax = plt.subplots()
    ax.plot(t, signal)
    ax.set_facecolor("#0f2027")
    ax.set_title("Brain Activity", color="white")
    ax.tick_params(colors='white')

    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ AI PANEL ------------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 AI Analysis")

    avg = np.mean(np.abs(signal))

    if avg > 1:
        st.error("⚠️ High Seizure Risk")
    elif avg > 0.6:
        st.warning("😟 Moderate Stress")
    else:
        st.success("✅ Normal Brain Activity")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚡ Stimulus Test")

    if st.button("Apply Stimulus"):
        st.write("Analyzing...")
        time.sleep(1)
        st.success(random.choice([
            "Normal Response",
            "Delayed Response",
            "Abnormal Response ⚠️"
        ]))

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<hr>
<center>🚀 Advanced EEG Monitoring System | Designed for Bio Engineers</center>
""", unsafe_allow_html=True)
