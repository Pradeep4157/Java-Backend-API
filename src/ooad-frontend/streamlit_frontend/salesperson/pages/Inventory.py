import streamlit as st
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/inventory/"

def fetch_inventory():
    """
    Function to fetch inventory data from the API.
    """
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch inventory data. Please try again later.")
        return []

def add_inventory(carmodel):
    """
    Function to add inventory item via the API.
    """
    url = BASE_URL + f"add/{carmodel}"
    response = requests.post(url)

def remove_inventory(carmodel):
    """
    Function to remove inventory item via the API.
    """
    url = BASE_URL + f"remove/{carmodel}"
    response = requests.post(url)

def main():
    st.title("Inventory Management System")
    
    # Fetch inventory data
    inventory_data = fetch_inventory()
    
    # Display inventory data in a table
    if inventory_data:
        st.write("Current Inventory:")
        for item in inventory_data:
            st.write(f"**Item** : {item['carModel']}")
            st.write(f"**Units** : {item['units']}")
            # Buttons to add and remove inventory items
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Add {item['carModel']}"):
                    add_inventory(item['carModel'])
            with col2:
                if st.button(f"Remove {item['carModel']}"):
                    remove_inventory(item['carModel'])
            st.write("---")
    else:
        st.warning("No inventory items found.")

if __name__ == "__main__":
    main()
