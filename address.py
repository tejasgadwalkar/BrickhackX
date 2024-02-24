import requests

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
    
def main():
	api_key = "AIzaSyBGJDglC3cgmg3graBro0l4fMJmXj-XNhg"

	# Example usage:
	addressStart = "14 Meeting House Dr, Rochester, NY 14624"
	addressEnd = "160 Keller St, Rochester, NY 14609"
	time = get_driving_time(api_key, addressStart, addressEnd)
	print(time)
    

main()