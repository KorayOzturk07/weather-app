# Weather App 🌤️

A sleek, responsive weather application built with Flask and OpenWeatherMap API that provides current weather conditions for any city worldwide.

## Features ✨

- Real-time weather data including:
  - Current temperature (°C)
  - "Feels like" temperature
  - Weather description
  - Humidity
  - Wind speed
  - Atmospheric pressure
  - Sunrise/sunset times
- Beautiful weather icons matching current conditions
- Smooth animations and transitions
- Fully responsive design (works on mobile, tablet, and desktop)
- Error handling for invalid city names
- Clean, modern UI with glass morphism effect

## Technologies Used 🛠️

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, Weather Icons
- **API**: OpenWeatherMap
- **Animations**: Animate.css

## Installation Guide 📥

### Prerequisites
- Python 3.6+
- pip package manager
- OpenWeatherMap API key (free tier available)

### Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/KorayOzturk07/weather-app.git
   cd weather-app
   ```
2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install flask requests python-dotenv
   ```
4. Create a `.env` file in the root directory:
   ```
   API_KEY=your_openweathermap_api_key_here
   FLASK_ENV=development
   ```
5. Run the application:
   ```
   python main.py
   ```
6. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## Configuration ⚙️
You can customize the following in `main.py`:

- Temperature unit (metric/imperial)
- Language for weather descriptions
- Default city

## API Reference 🌐
This application uses the OpenWeatherMap Current Weather Data API.

Required parameters:
- `q`: City name
- `appid`: Your API key
- `units`: Temperature unit (metric/imperial)
- `lang`: Response language

## Contributing 🤝
Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏
- Weather data provided by OpenWeatherMap
- Icons by Weather Icons
- Animations by Animate.css
