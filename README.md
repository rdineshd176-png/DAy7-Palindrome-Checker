# 🌦️ Weather App (Python Console)
This is **Day 6** of my 100 Days, 100 Projects in Python Challenge 🚀  

A simple **Weather App** built with Python that fetches **real-time weather data** from the OpenWeatherMap API.  
This is my **Day 6/100 Project** in the "100 Days, 100 Projects in Python" challenge 🚀

---

## ✨ Features
- Get live weather details by entering any city name
- Shows:
  - 🌡️ Temperature (Celsius)
  - 🤔 Feels Like Temperature
  - 💧 Humidity
  - 🌬️ Wind Speed
  - Weather Condition (Sunny, Rainy, Cloudy, etc.)
- Loop mode → check multiple cities
- Exit anytime by typing `exit`

---

## 🛠️ Requirements
- Python 3.x
- [Requests](https://pypi.org/project/requests/) library

Install requests:
```bash
pip install requests
Go to this https://home.openweathermap.org site and get the api and past it the weatherapi.py api = your api key 
python weatherapi.py

Enter city name (or 'exit' to quit): Chennai

Weather in Chennai: Clear Sky
🌡️ Temperature: 32°C
🤔 Feels like: 34°C
💧 Humidity: 60%
🌬️ Wind Speed: 2.5 m/s
