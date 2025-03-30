import requests

API_KEY = "API KEY BURAYA GELİYOR !!!"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
}
        
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return f"{city_name}: {temperature}°C\n{description.capitalize()}\nNem Oranı: {humidity}\nRüzgar Hızı: {wind_speed}"

    else:
        return "Şehir bilgisi bulunamadı\nŞehir adını kontrol ediniz"