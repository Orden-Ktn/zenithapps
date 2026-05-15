import requests
from django.shortcuts import render

def LandInfo(request):
    url = "https://restcountries.com/v3.1/all?fields=name,flags,capital,continents,languages,currencies"

    response = requests.get(url)
    data = response.json()

    countries = []

    if isinstance(data, list):
        for country in data:
            countries.append({
                'name': country.get('name', {}).get('common', 'N/A'),
                'flag': country.get('flags', {}).get('png', ''),
                'capital': country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A',
                'continent': country.get('continents', ['N/A'])[0],
                'language': list(country.get('languages', {}).values())[0]
                            if country.get('languages') else 'N/A',
                'currency': list(country.get('currencies', {}).keys())[0]
                            if country.get('currencies') else 'N/A',
            })

    countries = sorted(countries, key=lambda x: x['name'])

    return render(request, 'LandInfo.html', {'countries': countries})