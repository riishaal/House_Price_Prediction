import streamlit as st
import pickle
import numpy as np

# Load model and features
with open("model.pkl", "rb") as f:
    model, feature_names = pickle.load(f)

st.title("🏠 House Price Predictor")

# User input form
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)
sqft_living = st.number_input("Living Area (sqft)", 200, 10000, 1500)
sqft_lot = st.number_input("Lot Area (sqft)", 500, 20000, 5000)
floors = st.selectbox("Floors", [1, 1.5, 2, 2.5, 3])
waterfront = st.selectbox("Waterfront", [0, 1])
view = st.slider("View (0–4)", 0, 4, 0)
condition = st.slider("Condition (1–5)", 1, 5, 3)
sqft_above = st.number_input("Sqft Above Ground", 200, 10000, 1200)
sqft_basement = st.number_input("Sqft Basement", 0, 5000, 300)
yr_built = st.number_input("Year Built", 1900, 2025, 2000)
yr_renovated = st.number_input("Year Renovated", 0, 2025, 0)
city = st.number_input("City Code", 0, 100, 0)  # Encoded
statezip = st.number_input("Zip Code Code", 0, 100, 0)  # Encoded

# Prepare input for prediction
input_data = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                        waterfront, view, condition, sqft_above, sqft_basement,
                        yr_built, yr_renovated, city, statezip]])

# Predict
if st.button("Predict Price"):
    price = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: ₹{int(price):,}")
