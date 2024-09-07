import streamlit as st
import requests
import random
from datetime import datetime
import time

# Define the base URL for the API
BASE_URL = "http://localhost:5000/"

# Function to browse cars
def browse_cars():
    st.title("Browse Cars")
    response = requests.get(BASE_URL + "cars/")
    if response.status_code == 200:
        cars = response.json()
        if cars:
            st.write("Available Cars:")
            car_data = []
            for car in cars:
                car_data.append({
                    "Car ID": car['carId'],
                    "Manufacturer": car['carManufacturer'],
                    "Model": car['carModel'],
                    "Manufacture Year": car['manufactureYear']
                })
            st.table(car_data)
        else:
            st.write("No cars available.")
    else:
        st.error("Failed to fetch cars")

def make_purchase(purchase):
    url = "http://localhost:5000/purchases/makepurchase"
    response = requests.post(url, json=purchase)
    return response

def purchase_car():
    st.title("Purchase Car")
    # Input fields for purchase details
    purchase_id = random.randint(10000, 99999)
    car_id = st.number_input("Car ID", min_value=1, step=1)
    customer_id = st.number_input("Customer ID", min_value=1, step=1)
    payment_id = st.number_input("Payment ID", min_value=1, step=1)
    purchase_date = st.date_input("Purchase Date")
    
    purchase = {
        "purchaseID": purchase_id,
        "carId": car_id,
        "customerId": customer_id,
        "paymentId": payment_id,
        "purchaseDate": str(purchase_date)
    }
    
    if st.button("Purchase"):
        response = make_purchase(purchase)
        if response.status_code == 201:
            st.success("Car purchased successfully!")
        elif response.status_code == 400:
            st.error("Purchase ID already exists. Please choose a different ID.")
        else:
            st.error("Failed to purchase car. Please try again later.")

# Function to search for a specific car
def search_car():
    st.title("Search Car")
    car_id = st.number_input("Enter Car ID:", step=1, value=0)
    if st.button("Search"):
        response = requests.get(BASE_URL + f"cars/searchcar/{car_id}")
        if response.status_code == 200:
            car = response.json()
            st.write("# Car Details:")
            st.write(f"## Manufacturer: {car['carManufacturer']} \n ### Model: {car['carModel']} \n Manufacture Year: {car['manufactureYear']}")
        else:
            st.error("Car not found")

# Function to schedule a test drive
def schedule_test_drive():
    st.title("Schedule Test Drive")
    car_id = st.number_input("Enter Car ID:", value = 0,step = 1)
    date = st.date_input("Select Date:")
    time = st.time_input("Select Time:")
    if st.button("Schedule"):
        # Hardcoded customer ID
        customer_id = 1001
        
        # Generate random 5-digit appointment ID
        appointment_id = random.randint(10000, 99999)
        
        payload = {
            "appointmentId": appointment_id,
            "customerId": customer_id,
            "carId": car_id,
            "dateTime": f"{date}T{time}"
        }
        response = requests.post(BASE_URL + "/testdrives/scheduleTestDrive", json=payload)
        if response.status_code == 201:
            st.success("Test drive scheduled successfully")
            st.write("Ur Appointment : " + str(payload))
        else:
            st.error("Failed to schedule test drive")
            st.write(response)

def fetch_all_appointments():
    """
    Function to fetch all service appointments from the API.
    """
    url = BASE_URL
    response = requests.get(url + "servicerequest/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch appointments. Please try again later.")
        return []

def add_service_appointment(new_appointment):
    """
    Function to add a new service appointment via the API.
    """
    url = BASE_URL + "servicerequest/newappointment"
    response = requests.post(url, json=new_appointment)
    st.write(response)
    if response.status_code == 201:
        st.success("Service appointment added successfully")
    else:
        st.error("Failed to add service appointment")

def remove_service_appointment(appointment_id):
    """
    Function to remove a service appointment via the API.
    """
    url = BASE_URL + f"servicerequest/deleteappointment/{appointment_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        st.write(response.status_code)
        st.success("Service appointment removed successfully")
    else:
        st.write(response.text)
        st.error("Failed to remove service appointment")

def schedule_service():
    st.title("Service Appointment Management")

    # Fetch all service appointments
    appointments = fetch_all_appointments()

    # Display appointments
    if appointments:
        st.write("## All Service Appointments")
        for appointment in appointments:
            st.write(f"- Appointment ID: {appointment['appointmentId']}, Status: {appointment['status']}")
    else:
        st.warning("No service appointments found.")

    # Add appointment section
    st.header("Add Service Appointment")
    appointment_id = str(random.randint(10000, 99999))
    customer_id = st.number_input("Customer ID", min_value=1, step=1)
    car_id = st.number_input("Car ID", min_value=1, step=1)
    services = []
    total_cost = 0
    status = st.selectbox("Status", ["SCHEDULED"])
    updates = {}  # Initialize updates
    if st.button("Add Appointment"):
        new_appointment = {
            "appointmentId": appointment_id,
            "customerId": customer_id,
            "carId": car_id,
            "services": services,
            "totalCost": total_cost,
            "status": status,
            "updates": updates
        }
        add_service_appointment(new_appointment)

    # Remove appointment section
def delete_service():
    st.header("Remove Service Appointment")
    appointment_id_to_remove = st.number_input("Enter Appointment ID to remove", min_value=1, step=1)
    if st.button("Remove Appointment"):
        remove_service_appointment(appointment_id_to_remove)   

def add_service_to_appointment(appointment_id, service_type, description):
    url = f"{BASE_URL}servicerequest/add/service/{appointment_id}"
    payload = {
        "serviceType": service_type,
        "description": description
    }
    response = requests.post(url, json=payload)
    return response

def remove_service_from_appointment(appointment_id, service_type, cost, description):
    url = f"{BASE_URL}servicerequest/remove/service/{appointment_id}"
    payload = {
        "serviceType": service_type,
        "description": description
    }
    response = requests.post(url, json=payload)
    return response

def get_services_for_appointment(appointment_id):
    url = f"http://localhost:5000/servicerequest/getappointment/{appointment_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('services', [])
    else:
        return []

def manage_service():
    st.title("Manage Services for Appointment")
    
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

    st.header("Add Service")
    service_type = st.selectbox("Service Type", ["CLEANING", "FITTING", "PAINTING", "REPAIR"])
    description = st.text_input("Description")

    # Button to add service
    if st.button("Add Service"):
        if appointment_id and service_type and description:
            response = add_service_to_appointment(appointment_id, service_type, description)
            st.write(response.text)
            if response.status_code == 201:
                st.success("Service added successfully!")
                time.sleep(1)
                st.experimental_rerun()
            else:
                st.error("Failed to add service. Please try again later.")
        else:
            st.warning("Please fill in all the fields.")
    
    # Input fields for removing a service
    st.header("Remove Service")
    service_type_to_remove = st.selectbox("Service Type to Remove", ["CLEANING", "FITTING", "PAINTING", "REPAIR"])
    description_to_remove = st.text_input("Description to Remove")
    
    # Button to remove service
    if st.button("Remove Service"):
        if appointment_id and service_type_to_remove and description_to_remove:
            response = remove_service_from_appointment(appointment_id, service_type_to_remove, description_to_remove)
            st.write(response.text)
            if response.status_code == 200:
                st.success("Service removed successfully!")
                time.sleep(1)
                st.experimental_rerun()
            else:
                st.error("Failed to remove service. Please try again later.")
        else:
            st.warning("Please fill in all the fields.")


# Sidebar navigation
page = st.sidebar.selectbox("Select Page", ["Browse Cars", "Search Car","Buy Car", "Schedule Test Drive", "Schedule Service","Delete Service Request","Manage Service"])

# Render the selected page
if page == "Browse Cars":
    browse_cars()
elif page == "Search Car":
    search_car()
elif page == "Buy Car":
    purchase_car()
elif page == "Schedule Test Drive":
    schedule_test_drive()
elif page == "Schedule Service":
    schedule_service()
elif page == "Delete Service Request":
    delete_service()
elif page == "Manage Service":
    manage_service()