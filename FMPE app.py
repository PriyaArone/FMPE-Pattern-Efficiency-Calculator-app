
import streamlit as st
import numpy as np

def calculate_ploughing_efficiency(w, f, Sp, Se, n, L, W):
    # Convert speed from km/h to m/s
    Sp = Sp * (1000 / 3600)
    Se = Se * (1000 / 3600)

    # Basic calculations
    trips = W / w  # Number of trips
    time_per_furrow = f / Sp / 3600  # Convert seconds to hours
    total_ploughing_time = trips * time_per_furrow

    # Turning calculations
    turning_time = (trips / n) * (f / Se / 3600)  # Convert seconds to hours
    total_time = total_ploughing_time + turning_time

    # Efficiencies
    pattern_efficiency = (W * L) / (trips * w * f) * 100
    processing_efficiency = (total_ploughing_time / total_time) * 100

    return total_time, processing_efficiency, pattern_efficiency

# Streamlit App
st.title("Ploughing Efficiency Calculator")

# Input Fields
w = st.number_input("Effective width of plough (m)", min_value=0.1, value=1.2)
f = st.number_input("Furrow length (m)", min_value=1, value=100)
Sp = st.number_input("Speed of ploughing (km/h)", min_value=0.1, value=6.4)
Se = st.number_input("Speed around ends (km/h)", min_value=0.1, value=8.0)
n = st.number_input("Number of back-furrowed lands", min_value=1, value=4)
L = st.number_input("Field length (m)", min_value=1, value=400)
W = st.number_input("Field width (m)", min_value=1, value=100)

if st.button("Calculate"):
    total_time, processing_efficiency, pattern_efficiency = calculate_ploughing_efficiency(w, f, Sp, Se, n, L, W)

    st.write(f"### Total Ploughing Time: {total_time:.2f} hours")
    st.write(f"### Processing Efficiency: {processing_efficiency:.2f}%")
    st.write(f"### Pattern Efficiency: {pattern_efficiency:.2f}%")
