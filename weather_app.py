import requests
from dotenv import load_dotenv
load_dotenv()
import os

def get_weather(city):
    api_key = os.getenv('API_KEY')
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    data = response.json()
    # Parse and print relevant data
    temperature = data['current']['temperature']
    print(f"Current temperature in {city} is: {temperature}°C")

if __name__ == "__main__":
    while True:
        try:
            city = input("Enter the name of the city: (Press 0 to exit) ")
            if city != "0":
                get_weather(city)
            else:
                break
        except KeyError:
            print("Invalid city")

