import streamlit as st
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/"

def fetch_all_appointments():
    """
    Function to fetch all service appointments from the API.
    """
    url = BASE_URL
    response = requests.get(url + "servicerequest/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch appointments. Please try again later.")
        return []
    
st.title("Service Appointment Management")

# Fetch all service appointments
appointments = fetch_all_appointments()

# Display appointments
if appointments:
    st.write("## All Service Appointments")
    for appointment in appointments:
        st.write(f"- Appointment ID: {appointment['appointmentId']}, Status: {appointment['status']}")
else:
    st.warning("No service appointments found.")