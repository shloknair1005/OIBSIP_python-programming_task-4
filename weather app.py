import requests

API_KEY = "b5d11711583a032da8009a55ba933901"
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {data["name"]}, {data["sys"]["country"]}")
        print(f"\nTemperature: {data["main"]["temp"]} Celsius")
        print(f"\nHumidity: {data["main"]["humidity"]}%")
        print(f"\nWeather: {data["weather"][0]["description"].title()}")
    else:
        print("City not found")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)