import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('california_housing_model.pkl')

# Streamlit app interface
st.title("California Housing Price Prediction App")
st.write("Enter the house features to get a predicted price:")

# Collect user input for prediction
MedInc = st.number_input("Median Income (in $10,000s):", min_value=0.0, max_value=20.0, value=3.0)
HouseAge = st.number_input("House Age (in years):", min_value=0, max_value=100, value=30)
AveRooms = st.number_input("Average Number of Rooms:", min_value=0.0, max_value=50.0, value=5.0)
AveBedrms = st.number_input("Average Number of Bedrooms:", min_value=0.0, max_value=10.0, value=1.0)
Population = st.number_input("Population:", min_value=0, max_value=50000, value=1000)
AveOccup = st.number_input("Average Occupancy:", min_value=0.0, max_value=10.0, value=3.0)
Latitude = st.number_input("Latitude:", min_value=32.0, max_value=42.0, value=34.0)
Longitude = st.number_input("Longitude:", min_value=-125.0, max_value=-114.0, value=-120.0)

# Predict button
if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    prediction = model.predict(input_data)
    st.write(f"Predicted House Price: ${prediction[0] * 1000:.2f}")
