import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("House Price Prediction App")

st.write("Enter house details:")

# User inputs
MedInc = st.number_input("Median Income", 0.0, 20.0, 3.0)
HouseAge = st.number_input("House Age", 0, 100, 10)
AveRooms = st.number_input("Average Rooms", 1.0, 20.0, 5.0)
AveBedrms = st.number_input("Average Bedrooms", 0.5, 10.0, 1.0)
Population = st.number_input("Population", 0, 50000, 1000)
AveOccup = st.number_input("Average Occupancy", 1.0, 10.0, 3.0)
Latitude = st.number_input("Latitude", 30.0, 45.0, 34.0)
Longitude = st.number_input("Longitude", -125.0, -110.0, -118.0)

# Predict button
if st.button("Predict Price"):
    
    input_data = pd.DataFrame({
        'MedInc': [MedInc],
        'HouseAge': [HouseAge],
        'AveRooms': [AveRooms],
        'AveBedrms': [AveBedrms],
        'Population': [Population],
        'AveOccup': [AveOccup],
        'Latitude': [Latitude],
        'Longitude': [Longitude]
    })
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted House Price: {prediction[0]:.2f}")