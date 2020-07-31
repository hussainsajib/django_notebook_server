from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('', HomeView, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
