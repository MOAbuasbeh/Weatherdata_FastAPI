import  requests

API_KEY = "687a39206f02401ab92161351260905"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
def fetch_data(city : str):
    params = {
        "key":API_KEY ,
         "q":city
    }
    response = requests.get(BASE_URL ,params = params)
    data = response.json()

    current = data['current']
    location = data['location']

    return {
        "city": location["name"],
        "country":location["country"],
        "temperature": current["temp_c"],
        "humidity": current["humidity"],
        "weather_condition": current["condition"]["text"]
    }


