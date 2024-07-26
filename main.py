import requests
from gtts import gTTS
import json
import os
from playsound import playsound
from dotenv import load_dotenv

def configure():
    load_dotenv()

# Call configure function to load environment variables
configure()


while True:
    city = input('Enter city name: ')

    # Construct the URL with the API key
    url = f'https://api.weatherapi.com/v1/current.json?key={os.getenv("api_key")}&q={city}'

    r = requests.get(url)
    weatherdic = json.loads(r.text)
    W = weatherdic["current"]["temp_c"]
    F = weatherdic["current"]["wind_kph"]

    mytext = f'The current Temperature in {city} is {W} degree Celsius And wind in kilometers per hour is {F}'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("welcome.mp3")
    playsound("welcome.mp3")

    # Provide an option to exit the loop or terminate the program
    if city.lower() == "exit":
        break




