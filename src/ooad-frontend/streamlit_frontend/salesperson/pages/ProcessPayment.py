import streamlit as st
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/payments/"

def fetch_all_payments():
    """
    Function to fetch all payments from the API.
    """
    url = BASE_URL
    response = requests.get(url)
    st.write(response)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch payments. Please try again later.")
        return []

def process_payment(payment_id):
    """
    Function to process a payment via the API.
    st.write(payment_id)
    """
    st.write(payment_id)
    url = BASE_URL + f"processpayment/{payment_id}"
    response = requests.post(url)
    if response.status_code == 200:
        st.success("Payment processed successfully!")
    else:
        st.error("Failed to process payment. Please check the provided payment ID.")

def main():
    st.title("Payment Management")

    # Fetch all payments
    payments = fetch_all_payments()

    # Display payments
    if payments:
        st.write("## All Payments")
        for payment in payments:
            st.write(f"- Payment ID: {payment['paymentId']}, Status: {payment['paymentStatus']}")
    else:
        st.warning("No payments found.")

    # Process payment section
    st.header("Process Payment")
    payment_id = st.number_input("Payment ID", step=1, value=0)
    if st.button("Process Payment"):
        if payment_id:
            process_payment(payment_id)
            st.experimental_rerun()
        else:
            st.warning("Please enter a payment ID.")

if __name__ == "__main__":
    main()
