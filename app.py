import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="EEG Monitoring", layout="wide")

st.title("🧠 EEG Monitoring System")
st.write("Simple Prototype for Brain Signal Detection")

# Sidebar
wave_type = st.sidebar.selectbox(
    "Select Brain Wave",
    ["Alpha", "Beta", "Theta", "Delta"]
)

# Generate signal
t = np.linspace(0, 10, 500)

if wave_type == "Alpha":
    signal = np.sin(2 * np.pi * 10 * t)
elif wave_type == "Beta":
    signal = np.sin(2 * np.pi * 20 * t)
elif wave_type == "Theta":
    signal = np.sin(2 * np.pi * 6 * t)
else:
    signal = np.sin(2 * np.pi * 2 * t)

# Add noise
signal = signal + np.random.normal(0, 0.3, len(t))

# Plot
st.subheader("📊 EEG Signal")
fig, ax = plt.subplots()
ax.plot(t, signal)
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
st.pyplot(fig)

# Simple AI logic
st.subheader("🤖 Analysis")

avg = np.mean(np.abs(signal))

if avg > 1:
    st.error("⚠️ High Risk")
elif avg > 0.6:
    st.warning("😟 Medium Stress")
else:
    st.success("😊 Normal")

# Stimulus
st.subheader("⚡ Stimulus Test")

if st.button("Apply Stimulus"):
    st.write("Applying stimulus...")
    time.sleep(1)
    st.success(random.choice([
        "Normal Response",
        "Abnormal Response",
        "Delayed Response"
    ]))
