import requests
import json

file = json.load(open("key.json"))
api_key = file["key"]


def get_driving_time(origin, destination):
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
            driving_time = data["rows"][0]["elements"][0]["duration"]["text"]
            return to_int_driving_time(driving_time)
        else:
            error_message = data["error_message"] if "error_message" in data else "Unknown error"
            raise Exception(f"Google Maps API error: {error_message}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def to_int_driving_time(passedTime):
    stringedTime = passedTime.split(" ")
    integerTime = 0

    if (len(stringedTime) == 4):
        if (stringedTime[1] == "hours" and stringedTime[3] == "mins"):
            integerTime = (int(stringedTime[0]) * 60) + int(stringedTime[2])
        elif (stringedTime[1] == "days" and stringedTime[3] == "hours"):
            integerTime = (int(stringedTime[0]) * 24 * 60) + (int(stringedTime[2]) * 60)
        elif (stringedTime[1] == "days" and stringedTime[3] == "mins"):
            integerTime = (int(stringedTime[0]) * 24 * 60) + int(stringedTime[2])
    elif (len(stringedTime) == 6):
        integerTime = (int(stringedTime[0]) * 24 * 60) + (int(stringedTime[2]) * 60) + int(stringedTime[4])
    else:
        if (stringedTime[1] == "hours"):
            integerTime = (int(stringedTime[0]) * 60)
        elif (stringedTime[1] == "days"):
            integerTime = (int(stringedTime[0]) * 24 * 60)
        else:
            integerTime = int(stringedTime[0])
        
    return int(integerTime)



#
# def address_exists(address):
#     url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
#     params = {
#         "key": api_key,
#         "input": address,
#         "inputtype": "textquery",
#         "fields": "formatted_address"
#     }
#
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#
#         if data["status"] == "OK" and data.get("candidates"):
#             return True
#         else:
#             return False
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False
#


def validate_address(ad):
    # Google Geocoding API endpoint
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address': ad,
        'key': api_key
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    if data['status'] == 'OK':
        # Extract the validated address information
        formatted_address = data['results'][0]['formatted_address']
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']

        # print(f"Validated Address: {formatted_address}")
        # print(f"Latitude: {latitude}, Longitude: {longitude}")
        return formatted_address
    else:
        print("Address validation failed.")
        return "Address DNE"
     
    
if __name__ == '__main__':

    # Example usage:
    # addressStart = "14 Meeting House Dr, Rochester, NY 14624"
    addressStart = "RIT one lomb drive rochester NY"
    addressEnd = "160 Keller St, Rochester, NY 14609"
    time1 = get_driving_time(addressStart, addressEnd)
    time2 = get_driving_time(addressEnd, addressStart)

    print(validate_address(addressStart))
    print(validate_address(addressEnd))
    print("Optimal driving time from A to B is", time1)
    print("Optimal driving time from B to A is", time2)
