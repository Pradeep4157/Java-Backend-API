import streamlit as st
import requests
from enum import Enum
# Base URL of the API
BASE_URL = "http://localhost:5000/engineer/"

# Define the enum for Status
class Status(Enum):
    SCHEDULED = "SCHEDULED"
    QUEUED = "QUEUED"
    COMPLETED = "COMPLETED"
    PICKUP_ALERT = "PICKUP_ALERT"

def update_status(appointment_id, status):
    try:
        # Make a PUT request to update the status
        response = requests.put(BASE_URL + f"{appointment_id}/updateStatus?status={status}")
        return response
    except Exception as e:
        st.error(f"Error updating status: {e}")
        return None

def main():
    st.title("Update Service Request Status")

    # Input fields
    appointment_id = st.number_input("Enter Appointment ID", min_value=1, step=1)
    status = st.selectbox("Select Status", [status.value for status in Status])

    if st.button("Update Status"):
        if appointment_id and status:
            response = update_status(appointment_id, status)
            if response and response.status_code == 200:
                st.success("Status updated successfully!")
            else:
                st.error("Failed to update status.")
        else:
            st.warning("Please fill in all the fields.")

if __name__ == "__main__":
    main()
