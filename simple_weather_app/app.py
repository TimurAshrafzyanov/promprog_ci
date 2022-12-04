from flask import Flask
from flask import request

import weather


app = Flask(__name__)

@app.route("/weather")
def get_weather():
    city = request.args.get('city', 'Sankt-Peterburg')
    return weather.get_weather(city)


@app.route("/")
def index():
    return "Welcome! The service takes a date and gives corresponding day of the week"

if __name__ == "__main__":
    app.run()
