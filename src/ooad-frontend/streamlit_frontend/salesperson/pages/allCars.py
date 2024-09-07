import streamlit as st
import requests
import pandas as pd

# API endpoint
API_URL = "http://localhost:5000/cars/"

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data from API. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Define a function to create a card
def create_card(car):
    st.write(f"# Model : {car['carModel']}")
    st.write(f"## From : {car['carManufacturer']}")
    st.write(f"##### ID : {car['carId']}")
    st.write(f"## Price : {car['quotedPrice']}")
    st.write(f"#### Insured By : {car['insuranceProvider']}")
    st.write(f"### Year of Manufacture : {car['manufactureYear']}")
    st.write("---")

def main():
    st.title("Cars Catalog")
    cars_data = fetch_data_from_api("http://localhost:5000/cars/")

    if cars_data:
        for car in cars_data:
            create_card(car)
        
if __name__ == "__main__":
    main()
