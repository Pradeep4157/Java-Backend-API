import streamlit as st
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/"

def update_service_progress(appointment_id, update):
    """
    Function to send a PUT request to the updateProgress endpoint.
    """
    url = BASE_URL + f"engineer/appointments/{appointment_id}/updateProgress"
    try:
        response = requests.put(url, json=update)
        return response
    except Exception as e:
        st.error(f"Error: {e}")
        st.write(response.text)
        return None

def main():
    st.title("Update Service Progress")

    # Input fields for appointment ID and update
    appointment_id = st.number_input("Appointment ID", min_value=1, step=1)
    update = st.text_area("Update")

    # Button to submit update
    if st.button("Update Progress"):
        if appointment_id and update:
            response = update_service_progress(appointment_id, update)
            if response and response.status_code == 200:
                st.success("Progress updated successfully!")
            else:
                st.error("Failed to update progress. Please try again later.")
                st.write(response.text)
        else:
            st.warning("Please fill in all the fields.")

if __name__ == "__main__":
    main()

