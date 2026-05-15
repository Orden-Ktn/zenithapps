from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('VorteKey/', include('VorteKey.urls')),
    path('DeviZio/', include('DeviZio.urls')),
    path('LandInfo/', include('LandInfo.urls')),
    path('SkyView/', include('SkyView.urls')),
]
