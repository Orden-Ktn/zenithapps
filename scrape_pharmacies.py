import os
import django
import requests
from bs4 import BeautifulSoup
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZenithApps.settings')
django.setup()

from PharmaBenin.models import Pharmacy

url = "https://www.ubphar.com/content/ubphar/liste-des-pharmacies"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")


for table in tables:
    rows = table.find_all("tr")

    for row in rows[1:]:
        cols = row.find_all("td")

        if len(cols) >= 4:
            name = cols[0].get_text(strip=True)
            doctor = cols[1].get_text(strip=True)
            phone = cols[2].get_text(strip=True)
            city = cols[-2].get_text(strip=True)
            address = cols[-1].get_text(strip=True)

            full_text = row.get_text(" ", strip=True)

            Pharmacy.objects.create(
                name=name,
                doctor=doctor,
                phone=phone,
                city=city,
                address=address,
            )

            print(f"{name} ajouté")

        elif len(cols) == 3:
            name = cols[0].get_text(strip=True)
            city = cols[1].get_text(strip=True)
            address = cols[2].get_text(strip=True)

            full_text = row.get_text(" ", strip=True)

            Pharmacy.objects.create(
                name=name,
                doctor="Non précisé",
                phone="Non précisé",
                city=city,
                address=address            )

            print(f"{name} ajouté (partiel)")