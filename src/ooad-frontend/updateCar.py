import streamlit as st
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/"

def get_car_data(car_id):
    """
    Function to fetch the current data of a car using the provided car ID.
    """
    url = BASE_URL + f"cars/searchcar/{car_id}"
    response = requests.get(url)
    return response.json()

def update_car(car_id, car_data):
    """
    Function to make a request to update a car using the provided car ID and data.
    """
    url = BASE_URL + f"cars/updatecar/{car_id}"
    response = requests.post(url, json=car_data)
    return response

def main():
    st.title("Update Car UI")
    st.write("Enter the ID of the car you want to update:")
    
    # Input field for the car ID
    car_id = st.text_input("Car ID")
    
    if st.button("Fetch Car Data"):
        # Check if car ID is provided
        if car_id:
            # Fetch car data from the API
            car_data = get_car_data(car_id)
            if car_data:
                # Render form with fetched car data
                st.write("Update Car Details:")
                car_model = st.text_input("Car Model", value=car_data.get("carModel"))
                car_manufacturer = st.text_input("Car Manufacturer", value=car_data.get("carManufacturer"))
                quoted_price = st.number_input("Quoted Price", value=car_data.get("quotedPrice"))
                insurance_provider = st.text_input("Insurance Provider", value=car_data.get("insuranceProvider"))
                manufacture_year = st.number_input("Manufacture Year", value=car_data.get("manufactureYear"))
                
                if st.button("Update Car"):
                    # Create a dictionary containing the updated car data
                    updated_car_data = {
                        "carId": int(car_id),
                        "carModel": car_model,
                        "carManufacturer": car_manufacturer,
                        "quotedPrice": quoted_price,
                        "insuranceProvider": insurance_provider,
                        "manufactureYear": manufacture_year
                    }
                    response = update_car(car_id, updated_car_data)
                    st.write(response)
                    if response.status_code == 201:
                        st.success(f"Car with ID {car_id} successfully updated!")
                    elif response.status_code == 404:
                        st.error("Car not found. Please check the provided ID.")
                    else:
                        st.error("Failed to update car. Please try again later.")
            else:
                st.error("Car not found. Please check the provided ID.")
        else:
            st.warning("Please enter a valid car ID.")
main()
