import streamlit as st
import requests
import pandas as pd

# Function to fetch data from the API endpoint
def fetch_data():
    url = "http://localhost:5000/cars/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main function to run the Streamlit app
def main():
    st.title("Car Data Viewer")
    
    # Fetching data from the API endpoint
    data = fetch_data()
    
    if data is not None:
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Display the DataFrame as a table
        st.write(df)
    else:
        st.error("Failed to fetch data from the API")

if __name__ == "__main__":
    main()
