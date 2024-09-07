import streamlit as st
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/"

def fetch_all_appointments():
    """
    Function to fetch all appointments from the API.
    """
    url = BASE_URL + "testdrives/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch appointments. Please try again later.")
        return []

def clear_test_drive(appointment_id):
    """
    Function to clear a test drive appointment via the API.
    """
    url = BASE_URL + "testdrives/clearTestDrive"
    params = {"appointmentId": appointment_id}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        st.success("Test drive appointment cleared successfully!")
        st.experimental_rerun()
    else:
        st.error("Failed to clear test drive appointment. Please try again later.")

def main():
    st.title("Test Drive Management")

    # Show all appointments section
    st.header("All Appointments")
    all_appointments = fetch_all_appointments()
    if all_appointments:
        st.write("## All Appointments")
        for appointment in all_appointments:
            st.write(f"- Appointment ID: {appointment['appointmentId']}, Details: {appointment}")
    else:
        st.warning("No appointments found.")

    # Clear test drive section
    st.header("Clear Test Drive")
    appointment_id = st.number_input("Enter Appointment ID to clear", step=1, value=0)
    if st.button("Clear Test Drive"):
        if appointment_id > 0:
            clear_test_drive(appointment_id)
        else:
            st.warning("Please enter a valid Appointment ID.")
main()
