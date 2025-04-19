# WeatherAPP

A simple Flask web app that shows real-time weather info by city using the OpenWeatherMap API.

------------------------
FEATURES
------------------------
- Search weather by city name
- Shows temperature, humidity, and description
- Built with Flask and Requests
- Uses .env file to keep API key secure

------------------------
TECH STACK
------------------------
- Python 3.10+
- Flask
- Requests
- Gunicorn (for deployment)
- Render (as host)

------------------------
HOW TO RUN LOCALLY
------------------------

1. Clone this repo:
   git clone https://github.com/Fakhrul-Hakimy/WeatherAPP.git
   cd WeatherAPP

2. Create a virtual environment (optional):
   python -m venv .venv
   .venv\Scripts\activate  (for Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Create a `.env` file in the project root:
   API_KEY=your_openweathermap_api_key_here

5. Run the app:
   python app.py

Then visit: http://127.0.0.1:5000/

------------------------
TESTING
------------------------

Run test:
   pytest

------------------------
LIVE DEMO
------------------------
Visit: https://weatherapp0909.onrender.com/

------------------------
PROJECT FILES
------------------------

app.py             ← main Flask app
test_app.py        ← test script
requirements.txt   ← dependencies
templates/index.html ← HTML template

------------------------
LICENSE
------------------------
MIT License – Free to use and modify

