from django import forms
from datetime import date
from Depenso.models import Expense
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'reason']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_date(self):
        d = self.cleaned_data['date']
        today = date.today()

        # Autoriser uniquement le mois en cours
        if d.year != today.year or d.month != today.month:
            raise forms.ValidationError(
                "La date doit être dans le mois en cours."
            )

        # PAS de blocage sur les jours passés ou futurs du mois
        return d
    

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "jean_dupont", "autocomplete": "username"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personnalisation des champs hérités de UserCreationForm
        self.fields["username"].label = "Nom d'utilisateur"
        self.fields["password1"].label = "Mot de passe"
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"placeholder": "Minimum 8 caractères", "autocomplete": "new-password"}
        )
        self.fields["password2"].label = "Confirmer le mot de passe"
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"placeholder": "Répétez le mot de passe", "autocomplete": "new-password"}
        )
        # Supprime les textes d'aide verbeux de Django
        for field in self.fields.values():
            field.help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email      = self.cleaned_data.get("email", "")
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nom d'utilisateur"
        self.fields["username"].widget = forms.TextInput(
            attrs={"placeholder": "Entrez votre identifiant", "autocomplete": "username"}
        )
        self.fields["password"].label = "Mot de passe"
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"placeholder": "Entrez votre mot de passe", "autocomplete": "current-password"}
        )
        for field in self.fields.values():
            field.help_text = None

