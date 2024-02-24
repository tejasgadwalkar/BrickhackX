import requests
import json

def get_driving_time(api_key, origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "key": api_key,
        "origins": origin,
        "destinations": destination,
        "mode": "driving"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data["status"] == "OK":
            print("data thingy is: ", data)
            driving_time = data["rows"][0]["elements"][0]["duration"]["text"]
            return driving_time
        else:
            error_message = data["error_message"] if "error_message" in data else "Unknown error"
            raise Exception(f"Google Maps API error: {error_message}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def address_exists(api_key, address):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "key": api_key,
        "input": address,
        "inputtype": "textquery",
        "fields": "formatted_address"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data["status"] == "OK" and data.get("candidates"):
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
    
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
     
    
def main():
  
  file = json.load(open("key.json"))
  api_key = file["key"]

	# Example usage:
	addressStart = "14 Meeting House Dr, Rochester, NY 14624"
	addressEnd = "160 Keller St, Rochester, NY 14609"
	time = get_driving_time(api_key, addressStart, addressEnd)
	print(time)

  # Example usage:
  address = "2 main st vestal, NY"
  validate_address(address)
  
main()