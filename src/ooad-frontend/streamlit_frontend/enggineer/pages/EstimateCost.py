import streamlit as st
import requests

# Base URL for the Java backend
BASE_URL = "http://localhost:5000"


def get_services_for_appointment(appointment_id):
    url = f"http://localhost:5000/servicerequest/getappointment/{appointment_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('services', [])
    else:
        return []
    
# Function to send POST request to estimate cost
def estimate_cost(appointment_id, estimate):
    """
    Function to send a POST request to the estimateCost endpoint.
    """
    url = BASE_URL + f"/engineer/appointments/{appointment_id}/estimateCost"
    try:
        response = requests.post(url, json=estimate)
        return response
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit app
def main():
    st.title("Car service details")
    
    # Input fields for appointment ID
    appointment_id = st.number_input("Appointment ID", min_value=1, step=1)
    
    # Fetch all services for the appointment ID
    services = get_services_for_appointment(appointment_id)
    
    if services:
        st.write("### All Services for Appointment:")
        service_table_data = []
        for service in services:
            service_info = {
                "Type": service['serviceType'],
                "Description": service['description']
            }
            service_table_data.append(service_info)
        
        # Display services in a table
        st.table(service_table_data)
    else:
        st.warning("No services found for the appointment.")

    estimate = st.number_input("Enter Estimate Cost:", value=0.0)

    # Button to submit estimate cost
    if st.button("Estimate Cost"):
        if appointment_id and estimate:
            response = estimate_cost(appointment_id, estimate)
            if response and response.status_code == 200:
                st.success("Estimate added successfully!")
            else:
                st.error("Failed to add estimate. Please try again later.")
        else:
            st.warning("Please fill in all the fields.")


if __name__ == "__main__":
    main()
