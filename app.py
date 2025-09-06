import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("rf_model.pkl")

st.title("Laptop Price Prediction App")

st.divider()

st.write(
    "With this app, after clicking the calculation button and entering values for "
    "Processor Speed, RAM Size, and Storage Capacity, you can get a price estimation "
    "for your laptop."
)

st.divider()

# User inputs
storage_capacity = st.number_input("Enter Storage Capacity (GB)", value=512, step=256)
ram_size = st.number_input("Enter RAM Size (GB)", value=16, step=8)
processor_speed = st.number_input("Enter Processor Speed (GHz)", value=2.50, step=0.50)

# Features in the SAME ORDER as training
X = [storage_capacity, ram_size, processor_speed]

st.divider()

prediction_btn = st.button("Price Estimation")

if prediction_btn:
    st.balloons()

    # DataFrame with correct feature names + order
    input_df = pd.DataFrame(
        [X],
        columns=["Storage_Capacity", "RAM_Size", "Processor_Speed"]
    )

    prediction = model.predict(input_df)[0]

    st.write(f" Estimated Price for the Laptop: **₹{prediction:,.2f}**")

else:
    st.write(" Please click the button for prediction.")
