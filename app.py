import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="EEG AI Monitor", layout="wide")

# -----------------------------
# Custom CSS (Modern UI)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #00f2ff;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("🧠 EEG AI Monitoring Dashboard")
st.write("Real-time neurological signal analysis system")

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("⚙️ Controls")

wave_type = st.sidebar.selectbox(
    "Brain Wave",
    ["Alpha", "Beta", "Theta", "Delta"]
)

# -----------------------------
# Generate Signal
# -----------------------------
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

# -----------------------------
# Layout (Columns)
# -----------------------------
col1, col2 = st.columns([2,1])

# -----------------------------
# EEG Chart
# -----------------------------
with col1:
    st.subheader("📊 Live EEG Signal")

    fig, ax = plt.subplots()
    ax.plot(t, signal)
    ax.set_facecolor("#0e1117")
    ax.set_title("Brain Signal", color="white")
    ax.tick_params(colors='white')

    st.pyplot(fig)

# -----------------------------
# AI Status Panel
# -----------------------------
with col2:
    st.subheader("🤖 AI Status")

    avg = np.mean(np.abs(signal))

    if avg > 1:
        status = "⚠️ High Seizure Risk"
    elif avg > 0.6:
        status = "😟 Moderate Stress"
    else:
        status = "✅ Normal"

    st.markdown(f'<div class="card">{status}</div>', unsafe_allow_html=True)

    st.subheader("⚡ Stimulus Test")
    if st.button("Apply Stimulus"):
        st.write("Analyzing...")
        time.sleep(1)
        st.success(random.choice([
            "Normal Response",
            "Delayed Response",
            "Abnormal Response ⚠️"
        ]))

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.write("Developed for Neurological Disorder Detection | EEG AI System")
