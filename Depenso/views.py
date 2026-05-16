from django.shortcuts import get_object_or_404, render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import RegisterForm, LoginForm



def register_view(request):
    # Redirige si déjà connecté
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connecte automatiquement après inscription
            login(request, user)
            messages.success(request, f"Bienvenue sur Depenso, {user.username} ! 🎉")
            return redirect("login")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = RegisterForm()

    return render(request, "Register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    
            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("dashboard")
        else:
            messages.error(request, "Identifiant ou mot de passe incorrect.")
    else:
        form = LoginForm()

    return render(request, "Login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Vous avez été déconnecté.")
    return redirect("login")



@login_required(login_url='login')
def Depenso(request):

    expenses = Expense.objects.filter(user=request.user).order_by('-date')

    form = ExpenseForm()

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "✅ Dépense ajoutée avec succès !")

            return redirect('dashboard')

    monthly_total = (
        Expense.objects
        .filter(user=request.user)
        .aggregate(total=Sum('amount'))
    )

    history = (
        Expense.objects
        .filter(user=request.user)
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('-month')
    )

    context = {
        'expenses': expenses,
        'form': form,
        'monthly_total': monthly_total,
        'history': history,
    }

    return render(request, 'Depenso.html', context)



@login_required(login_url='login')
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    # Vérifie que la dépense est dans le mois en cours
    now = timezone.now()
    if expense.date.month != now.month or expense.date.year != now.year:
        messages.error(request, "⛔ Modification impossible : cette dépense n'est pas du mois en cours.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Dépense modifiée avec succès !")
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)

    context = {'form': form, 'expense': expense}
    return render(request, 'Depenso.html', context)


@login_required(login_url='login')
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    now = timezone.now()
    if expense.date.month != now.month or expense.date.year != now.year:
        messages.error(request, "⛔ Suppression impossible : cette dépense n'est pas du mois en cours.")
        return redirect('dashboard')

    if request.method == 'POST':
        expense.delete()
        messages.success(request, "🗑️ Dépense supprimée.")
        return redirect('dashboard')

    return redirect('dashboard')


