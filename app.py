import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('car_mpg_model.pkl')

st.title("🚗 Car Mileage Predictor")
st.write("Enter the car details below to see how many miles per gallon (MPG) it will get.")
st.markdown("---")

horsepower = st.number_input("Horsepower", min_value=40, max_value=300, value=150)
weight = st.number_input("Weight (lbs)", min_value=1000, max_value=6000, value=3500)
displacement = st.number_input("Displacement (cu. in.)", min_value=50, max_value=500, value=300)

if st.button("Predict MPG"):
    new_car_data = pd.DataFrame(
        [[horsepower, weight, displacement]], 
        columns=['horsepower', 'weight', 'displacement']
    )
    prediction = model.predict(new_car_data)
    st.success(f"This car will likely get: {prediction[0]:.2f} MPG")