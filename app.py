import streamlit as st
import requests
import pandas as pd
import numpy as np

API_URL = st.secrets["API_URL"]
#
st.title("TaxiFare prediction")

st.write("Entrer ses informations pour avoir le cout du taxi.")

with st.form("prediction_form"):
    pickup_datetime = st.text_input(
        "Pickup datetime",
        value="2013-07-06 17:18:00 UTC"
    )

    pickup_longitude = st.number_input(
        "Pickup longitude", value=-73.950655, format="%.6f"
    )

    pickup_latitude = st.number_input(
        "Pickup latitude", value=40.783282, format="%.6f"
    )

    dropoff_longitude = st.number_input(
        "Dropoff longitude", value=-73.984365, format="%.6f"
    )

    dropoff_latitude = st.number_input(
        "Dropoff latitude", value=40.769802, format="%.6f"
    )

    passenger_count = st.number_input(
        "Passenger count", min_value=1, max_value=8, value=1
    )

    submitted = st.form_submit_button("Predict fare")

if submitted:
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count,
    }

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=params,
            timeout=30
        )

        response.raise_for_status()
        prediction = response.json()

        st.success(f"Cout Estimé: ${prediction['fare']:.2f}")

    except requests.exceptions.RequestException as error:
        st.error(f"API connection error: {error}")
