
import streamlit as st
import pandas as pd
import joblib

# 1. Load the trained model
model = joblib.load('traffic_model.pkl')

# 2. App Title and Description
st.title("🚦 Smart City: Traffic Volume Forecaster")
st.write("Predict real-time traffic volume based on weather and time.")

# 3. User Inputs (The "Sensors")
st.sidebar.header("Input Conditions")

# Time Inputs
hour = st.sidebar.slider("Hour of Day (0-23)", 0, 23, 12)
month = st.sidebar.slider("Month (1-12)", 1, 12, 7)

# Weather Inputs
temp = st.sidebar.number_input("Temperature (Kelvin)", value=280.0)
rain = st.sidebar.number_input("Rain (mm)", value=0.0)
clouds = st.sidebar.slider("Cloud Coverage (%)", 0, 100, 20)

# 4. Prediction Logic
if st.button("Predict Traffic Flow"):
    # Create a dataframe matching the format we trained on
    input_data = pd.DataFrame({
        'temp': [temp],
        'rain_1h': [rain],
        'clouds_all': [clouds],
        'hour': [hour],
        'month': [month]
    })

    # Get prediction
    prediction = model.predict(input_data)[0]
    
    # 5. Display Results
    st.metric(label="Predicted Traffic Volume", value=f"{int(prediction)} vehicles")

    # Visual Logic: Green/Yellow/Red based on volume
    if prediction < 1000:
        st.success("✅ Low Traffic - Roads are clear!")
    elif prediction < 4000:
        st.warning("⚠️ Moderate Traffic - Expect some delays.")
    else:
        st.error("🚨 High Traffic - Congestion likely.")