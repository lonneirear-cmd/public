import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("🌍 Climate Change & Biodiversity Dashboard")

st.markdown("## 📈 Global Temperature Rise")

# 가상 기온 데이터
years = np.arange(1980, 2023)
temperature = 0.02*(years-1980) + np.random.normal(0, 0.05, len(years))

fig, ax = plt.subplots()
ax.plot(years, temperature)
ax.set_xlabel("Year")
ax.set_ylabel("Temperature Anomaly (°C)")
ax.set_title("Global Temperature Rise")
st.pyplot(fig)


st.markdown("## 🐾 Species Decline Simulation")

temp_increase = st.slider("Temperature Increase (°C)", 0.0, 5.0, 1.0)

# 단순 가정 모델
species_loss = temp_increase * 10

st.write(f"Estimated species loss: {species_loss}%")

st.markdown("## 📊 Biodiversity Risk Level")

if temp_increase < 1.5:
    st.success("Low Risk")
elif temp_increase < 3:
    st.warning("Moderate Risk")
else:
    st.error("High Risk")
