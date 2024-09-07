import requests 
payload = {
    
}
response = requests.post(f"http://localhost:5000/cars/updatecar/{car.carId}", json=payload)