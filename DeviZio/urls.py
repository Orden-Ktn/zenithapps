from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviZio, name='DeviZio'),
]