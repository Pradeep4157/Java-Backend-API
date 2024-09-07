import streamlit as st
import requests

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

# Main function
def main():
    st.title("Booking Management System")

    # Sidebar option to select functionality
    selected_option = st.sidebar.selectbox("Select Functionality", ["Create Booking", "Delete Booking", "View Bookings"])

    # Create booking functionality
    if selected_option == "Create Booking":
        st.header("Create Booking")
        booking_id = st.number_input("Booking ID", min_value=1, step=1)
        customer_id = st.number_input("Customer ID", min_value=1, step=1)
        car_model = st.text_input("Car Model")
        if st.button("Create Booking"):
            if booking_id and customer_id and car_model:
                create_booking(booking_id, customer_id, car_model)
            else:
                st.warning("Please fill in all the fields.")

    # Delete booking functionality
    elif selected_option == "Delete Booking":
        st.header("Delete Booking")
        booking_id = st.number_input("Booking ID to delete", min_value=1, step=1)
        if st.button("Delete Booking"):
            if booking_id:
                delete_booking(booking_id)
            else:
                st.warning("Please enter the booking ID to delete.")

    # View bookings functionality
    elif selected_option == "View Bookings":
        st.header("View Bookings")

        # Fetch bookings from the backend API
        bookings = get_all_bookings()

        # Display bookings
        if bookings:
            st.write("## All Bookings")
            for booking in bookings:
                st.write(f"- Booking ID: {booking['bookingId']}, Customer ID: {booking['customerId']}, Car Model: {booking['carModel']}")
        else:
            st.warning("No bookings found.")

if __name__ == "__main__":
    main()
