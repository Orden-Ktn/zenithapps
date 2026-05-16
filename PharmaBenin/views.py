from django.shortcuts import render
from .models import Pharmacy

def PharmaBenin(request):

    query = request.GET.get('q')

    pharmacies = Pharmacy.objects.all()

    if query:
        pharmacies = pharmacies.filter(name__icontains=query)

    context = {
        'pharmacies': pharmacies
    }

    return render(request, 'PharmaBenin.html', context)