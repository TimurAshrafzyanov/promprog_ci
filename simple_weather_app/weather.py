import os
import requests


# Openweathermap API Token
APP_ID = os.environ.get('APP_ID', '')


def parse_weather(data):
    try:
        temp = data['main']['temp']
        return f'The temperature is: {float(temp)-273.15:.1f} degree'
    
    except Exception as e:
        return f'Data error: {e}'


def get_weather(city):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APP_ID}')
        if r.status_code != 200:
            return f'Invalid response code: {r.status_code}'
        else:
            return parse_weather(r.json())

    except Exception as e:
        return f'API error: {e}'
