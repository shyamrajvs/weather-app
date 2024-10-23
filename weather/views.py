import requests
from django.shortcuts import render
from .forms import CityForm

def weather_view(request):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    weather_data = {}
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found'}
    else:
        form = CityForm()
    
    context = {
        'form': form,
        'weather_data': weather_data
    }
    return render(request, 'weather/weather.html', context)
