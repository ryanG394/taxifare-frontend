import streamlit as st
import requests

API_URL = st.secrets["API_URL"]

st.title("TaxiFare prediction")

st.write("Enter your trip information to estimate the fare.")
