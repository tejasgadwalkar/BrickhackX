import json

import requests

file = json.load(open("Key.json"))
api_key = "AIzaSyAvtsdthq35gsokP2rfg8zCcL2x-uXuhJA"


def validate_address(ad):
    # Google Geocoding API endpoint
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'

    # API key (you'll need to replace 'YOUR_API_KEY' with your actual Google API key)

    # Parameters for the API request
    params = {
        'address': ad,
        'key': api_key
    }

    # Send GET request to the Google Geocoding API
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Check if the API request was successful
    if data['status'] == 'OK':
        # Extract the validated address information
        formatted_address = data['results'][0]['formatted_address']
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']

        print(f"Validated Address: {formatted_address}")
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        return True
    else:
        print("Address validation failed.")
        return False


# Example usage:
address = "2 main st vestal, NY"
validate_address(address)
