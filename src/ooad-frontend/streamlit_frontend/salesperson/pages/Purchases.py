# 16. http://localhost:5000/purchases/
# 17. http://localhost:5000/purchases/makepurchase
# 18. http://localhost:5000/purchases/deletepurchase/{purchaseid}
import streamlit as st
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/"

def fetch_all_purchases():
    """
    Function to fetch all purchases from the API.
    """
    url = BASE_URL + "purchases/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch purchases. Please try again later.")
        return []

def find_purchase(purchase_id):
    """
    Function to fetch a specific purchase from the API by its ID.
    """
    url = BASE_URL + f"purchases/findpurchase/{purchase_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        st.error("Purchase not found.")
        return None
    else:
        st.error("Failed to fetch purchase details. Please try again later.")
        return None

def main():
    st.title("Purchase Management")

    # Show all purchases section
    all_purchases = fetch_all_purchases()
    if all_purchases:
        st.write("## All Purchases")
        for purchase in all_purchases:
            st.write(f"- Purchase ID: {purchase['purchaseID']}, Details: {purchase}")
    else:
        st.warning("No purchases found.")

    # Find purchase by ID section
    st.header("Find Purchase by ID")
    purchase_id = st.number_input("Enter Purchase ID", step=1, value=0)
    if st.button("Find Purchase"):
        if purchase_id > 0:
            purchase_details = find_purchase(purchase_id)
            if purchase_details:
                st.write(f"### Purchase ID: {purchase_details['purchaseID']}")
                st.write(f"Details: {purchase_details}")
        else:
            st.warning("Please enter a valid Purchase ID.")
main()
