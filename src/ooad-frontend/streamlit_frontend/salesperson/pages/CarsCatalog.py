import streamlit as st
import requests
import random

# Function to create a booking
def create_booking(booking_id, customer_id, car_model):
    url = "http://localhost:5000/bookings/createBooking"
    payload = {
        "bookingId": booking_id,
        "customerId": customer_id,
        "carModel": car_model
    }
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        st.success("Booking created successfully!")
    else:
        st.error(f"Failed to create booking. Error: {response.text}")

# Function to delete a booking
def delete_booking(booking_id):
    url = f"http://localhost:5000/bookings/deleteBooking/{booking_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        st.success("Booking deleted successfully!")
    else:
        st.error(f"Failed to delete booking. Error: {response.text}")

# Function to fetch all bookings
def get_all_bookings():
    url = "http://localhost:5000/bookings/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch bookings. Error: {response.text}")

# Function to add a car
def add_car(car_data):
    try:
        payload = {
            "carId": car_data['carId'],
            "carManufacturer": car_data['carManufacturer'],
            "carModel": car_data['carModel'],
            "manufactureYear": car_data['manufactureYear'],
            "quotedPrice": car_data['quotedPrice'],
            "insuranceProvider": car_data['insuranceProvider']
        }
        response = requests.post("http://localhost:5000/cars/addcar", json=payload)
        response.raise_for_status()
        st.success("Car information submitted successfully!")
    except Exception as e:
        st.error("Error submitting car information: {}".format(e))

# Function to fetch car data
def get_car_data(car_id):
    url = "http://localhost:5000/cars/searchcar/" + car_id
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch car data for ID {car_id}. Error: {response.text}")

# Function to update car data
def update_car(car_id, car_data):
    url = "http://localhost:5000/cars/updatecar/" + car_id
    response = requests.post(url, json=car_data)
    if response.status_code == 201:
        st.success(f"Car with ID {car_id} successfully updated!")
    else:
        st.error(f"Failed to update car with ID {car_id}. Error: {response.text}")

# Function to remove a car
def remove_car(car_id):
    url = "http://localhost:5000/cars/removecar/" + car_id
    response = requests.delete(url)
    if response.status_code == 200:
        st.success(f"Car with ID {car_id} successfully removed!")
    else:
        st.error(f"Failed to remove car with ID {car_id}. Error: {response.text}")

# Function to create a card
def create_card(car):
    st.write(f"# Model : {car['carModel']}")
    st.write(f"## From : {car['carManufacturer']}")
    st.write(f"##### ID : {car['carId']}")
    st.write(f"## Price : {car['quotedPrice']}")
    st.write(f"#### Insured By : {car['insuranceProvider']}")
    st.write(f"### Year of Manufacture : {car['manufactureYear']}")
    st.write("---")

# Main function
def main():
    st.title("Car Catalog")
    selected_option = st.sidebar.selectbox("Select Functionality", ["Add Car", "Update Car", "Remove Car"])
    
    if selected_option == "Add Car":
        st.header("Add Car")
        car = {}
        car["carId"] = str(random.randint(10000, 99999))
        car["carManufacturer"] = st.text_input("Car Manufacturer")
        car["carModel"] = st.text_input("Car Model")
        car["manufactureYear"] = st.number_input("Manufacture Year", value=0)
        car["quotedPrice"] = st.number_input("Quoted Price", min_value=0.0)
        car["insuranceProvider"] = st.text_input("Insurance Provider")
        if st.button("Submit"):
            add_car(car)

    elif selected_option == "Update Car":
        st.header("Update Car")
        car_id = st.text_input("Car ID")
        if st.button("Fetch Car Data"):
            if car_id:
                car_data = get_car_data(car_id)
                if car_data:
                    st.write("Update Car Details:")
                    car_model = st.text_input("Car Model", value=car_data.get("carModel"))
                    car_manufacturer = st.text_input("Car Manufacturer", value=car_data.get("carManufacturer"))
                    quoted_price = st.number_input("Quoted Price", value=car_data.get("quotedPrice"))
                    insurance_provider = st.text_input("Insurance Provider", value=car_data.get("insuranceProvider"))
                    manufacture_year = st.number_input("Manufacture Year", value=car_data.get("manufactureYear"))
                    
                    if st.button("Update Car"):
                        updated_car_data = {
                            "carId": car_id,
                            "carModel": car_model,
                            "carManufacturer": car_manufacturer,
                            "quotedPrice": quoted_price,
                            "insuranceProvider": insurance_provider,
                            "manufactureYear": manufacture_year
                        }
                        update_car(car_id, updated_car_data)
                else:
                    st.error("Car not found. Please check the provided ID.")
            else:
                st.warning("Please enter a valid car ID.")

    elif selected_option == "Remove Car":
        st.header("Remove Car")
        car_id = st.text_input("Car ID")
        if st.button("Remove Car"):
            if car_id:
                remove_car(car_id)
            else:
                st.warning("Please enter a valid car ID.")
main()
