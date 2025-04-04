from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')

API_KEY = "a18ad2642f39f6e38cd8c4c05526bfcd"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        city_name = data["name"]
        temperature = round(data["main"]["temp"])
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        icon_code = data["weather"][0]["icon"]
        feels_like = round(data["main"]["feels_like"])
        pressure = data["main"]["pressure"]
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M')
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M')

        return {
            "city": city_name,
            "temperature": temperature,
            "description": description.capitalize(),
            "humidity": humidity,
            "wind_speed": wind_speed,
            "icon": icon_code,
            "feels_like": feels_like,
            "pressure": pressure,
            "sunrise": sunrise,
            "sunset": sunset,
            "time": datetime.now().strftime("%H:%M")
        }
    except requests.exceptions.RequestException:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if city:
            result = get_weather_data(city)
            if result:
                weather_data = result
            else:
                error = "Şehir bulunamadı. Lütfen geçerli bir şehir adı girin."
        else:
            error = "Lütfen bir şehir adı girin."
    
    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)