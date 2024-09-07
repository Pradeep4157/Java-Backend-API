import streamlit as st
import requests

# Function to check availability of cars by car model
def check_car_availability(car_model):
    # Send a GET request to the appropriate API endpoint
    response = requests.get(f"http://localhost:5000/inventory/checkavailable/{car_model}")
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        if data:
            st.write(f"Car Model: {data['carModel']}")
            st.write(f"Available Units: {data['units']}")
        else:
            st.write("No cars available for the specified model.")
    else:
        st.write("Failed to retrieve car availability information.")

# Streamlit app
def main():
    st.title("Check Car Availability")
    # Input field for entering car model
    car_model = st.text_input("Enter Car Model:")
    # Button to trigger the availability check
    if st.button("Check Availability"):
        if car_model:
            check_car_availability(car_model)
        else:
            st.write("Please enter a car model.")
main()