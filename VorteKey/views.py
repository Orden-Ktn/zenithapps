import random
import string

from django.shortcuts import render


def VorteKey(request):

    password = ""

    if request.method == "POST":

        length = int(request.POST.get('length', 12))

        uppercase = request.POST.get('uppercase')
        lowercase = request.POST.get('lowercase')
        numbers = request.POST.get('numbers')
        symbols = request.POST.get('symbols')

        characters = ""

        if uppercase:
            characters += string.ascii_uppercase

        if lowercase:
            characters += string.ascii_lowercase

        if numbers:
            characters += string.digits

        if symbols:
            characters += string.punctuation

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))

    context = {
        'password': password
    }

    return render(request, 'VorteKey.html', context)