import requests
from django.shortcuts import render


def DeviZio(request):

    result = None
    error = None

    currencies = [
        'USD', 'EUR', 'XOF', 'GBP',
        'JPY', 'CAD', 'CHF', 'CNY'
    ]

    # ✅ IMPORTANT : initialisation pour éviter l’erreur
    amount = ""
    from_currency = "EUR"
    to_currency = "USD"

    if request.method == 'POST':

        amount = request.POST.get('amount')
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        # SWAP
        if 'swap' in request.POST:
            from_currency, to_currency = to_currency, from_currency

        try:
            url = f"https://open.er-api.com/v6/latest/{from_currency}"
            response = requests.get(url)
            data = response.json()

            rate = data['rates'][to_currency]

            result = round(float(amount) * rate, 2)

        except Exception as e:
            error = str(e)

    return render(request, 'DeviZio.html', {
        'result': result,
        'error': error,
        'currencies': currencies,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount': amount
    })