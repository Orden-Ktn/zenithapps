from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='Depenso'),

    path('dashboard/', views.Depenso, name='dashboard'),

    path("inscription/", views.register_view, name="register"),

    path("login/", views.login_view, name="login"),

    path("deconnexion/", views.logout_view, name="logout"),

    path('depense/<int:pk>/update/', views.edit_expense,   name='edit_expense'),

    path('depense/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
]