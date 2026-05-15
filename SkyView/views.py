import requests
from django.shortcuts import render

API_KEY = "000faf1b1729921ff7ad6bec455c6634"

def SkyView(request):

    city = request.GET.get('city')

    weather_data = None

    if city:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:

            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
                'main': data['weather'][0]['main']
            }

    return render(request, 'SkyView.html', {
        'weather': weather_data
    })