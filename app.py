from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = os.getenv('API_KEY', 'your_openweather_api_key')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response.get('main'):
            weather = {
                'city': city,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'humidity': response['main']['humidity']
            }
            print(f"[DEBUG] Weather for {city}: {weather}")  # Terminal print
        else:
            print("[DEBUG] API response error:", response)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
