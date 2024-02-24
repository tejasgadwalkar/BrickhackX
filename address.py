import requests

def get_driving_time(api_key, origin, destination):
    """
    Get the driving time between two addresses using the Google Maps Distance Matrix API.

    Args:
        api_key (str): Your Google Maps API key.
        origin (str): The starting address.
        destination (str): The destination address.

    Returns:
        str: The driving time in text format (e.g., "1 hour 30 mins").
    """
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
        
        # Check if the API request was successful
        if data["status"] == "OK":
            # Extract the driving time
            driving_time = data["rows"][0]["elements"][0]["duration"]["text"]
            return driving_time
        else:
            # Handle API errors
            error_message = data["error_message"] if "error_message" in data else "Unknown error"
            raise Exception(f"Google Maps API error: {error_message}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    origin = "1600 Amphitheatre Parkway, Mountain View, CA"  # Example origin address
    destination = "350 5th Ave, New York, NY"  # Example destination address

    driving_time = get_driving_time(api_key, origin, destination)
    if driving_time:
        print(f"Driving time from {origin} to {destination} is: {driving_time}")


def address_exists(api_key, address):
    """
    Check if an address exists using the Google Maps Places API.

    Args:
        api_key (str): Your Google Maps API key.
        address (str): The address to check.

    Returns:
        bool: True if the address exists, False otherwise.
    """
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

        # Check if the API request was successful and at least one candidate is found
        if data["status"] == "OK" and data.get("candidates"):
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False