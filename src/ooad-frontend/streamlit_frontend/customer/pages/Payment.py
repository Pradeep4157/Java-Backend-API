import streamlit as st
import random
import requests

# Define the base URL for the API
BASE_URL = "http://localhost:5000/payments/makepayment/"

def make_payment(payment_mode):
    st.title("Make Payment")
    payment_id = random.randint(10000, 99999)
    purchase_id = st.number_input("Purchase ID", min_value=1, step=1)
    amount = st.number_input("Amount", min_value=0.0)
    payment_status = st.selectbox("Payment Status", ["PENDING"])
    
    if payment_mode == "Card":
        card_number = st.number_input("Card Number", min_value=0)
        holder_name = st.text_input("Holder Name")
        csv = st.number_input("CSV")
        expiry = st.text_input("Expiry")
        payment_data = {
            "_id": payment_id,
            "purchase_id": purchase_id,
            "amount": amount,
            "payment_status": payment_status,
            "payment_mode": payment_mode,
            "card_number": card_number,
            "holder_name": holder_name,
            "csv": csv,
            "expiry": expiry
        }
        
    elif payment_mode == "Cash":
        amount_collected = st.number_input("Amount Collected", min_value=0.0)
        date_time_collected = st.text_input("Date Time Collected")
        payment_data = {
            "_id": payment_id,
            "purchase_id": purchase_id,
            "amount": amount,
            "payment_status": payment_status,
            "payment_mode": payment_mode,
            "amount_collected": amount_collected,
            "date_time_collected": date_time_collected
        }
    elif payment_mode == "UPI":
        payer_upi_id = st.text_input("Payer UPI ID")
        payment_data = {
            "_id": payment_id,
            "purchase_id": purchase_id,
            "amount": amount,
            "payment_status": payment_status,
            "payment_mode": payment_mode,
            "payer_upi_id": payer_upi_id
        }
    
    # Make the payment
    if st.button("Make Payment"):
        try:
            # Send payment data to the API endpoint
            response = requests.post(BASE_URL + f"{payment_mode.lower()}", json=payment_data)
            st.write(response)
            if response.status_code == 201:
                st.success("Payment successful!")
            else:
                st.error("Failed to make payment. Please try again later.")
        except Exception as e:
            st.error(f"Error making payment: {e}")

def main():
    st.title("Payment Management")
    payment_mode = st.selectbox("Select Payment Mode", ["Card", "Cash", "UPI"])
    make_payment(payment_mode)

if __name__ == "__main__":
    main()
