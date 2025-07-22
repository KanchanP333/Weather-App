# Weather App 🌤️

A simple and elegant desktop weather application built with Python and PyQt5 that provides real-time weather information for any city worldwide.

## Features

- 🌍 Get weather data for any city globally
- 🌡️ Temperature display in Celsius
- 🎨 Clean and intuitive user interface
- 😊 Weather condition emojis for visual representation
- ⚡ Real-time weather updates
- 🔍 Detailed weather descriptions
- 💪 Robust error handling for various scenarios

## 🛠️ Technologies Used

- Python 3
- PyQt5
- Requests
- OpenWeatherMap API


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KanchanP333/weather-app.git
   cd weather-app
   ```

2. **Install required dependencies**
   ```bash
   pip install PyQt5 requests
   ```

   Or using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get an API key**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Get your free API key
   - Replace `"#"` in the code with your actual API key:
     ```python
     apiKey="#"
     ```

## Usage

1. **Run the application**
   ```bash
   python weather_app.py
   ```

2. **Using the app**
   - Enter a city name in the input field
   - Click "Get Weather" button
   - View the current temperature, weather emoji, and description

## API Integration

This app uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch real-time weather data. The app makes HTTP requests to:
```
https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}
```

