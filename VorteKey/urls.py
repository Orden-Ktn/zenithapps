from django.urls import path
from VorteKey import views


urlpatterns = [
    path('', views.VorteKey, name='VorteKey'),
]