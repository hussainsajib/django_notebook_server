from django.urls import path

from .views import HomeView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path('', HomeView, name='home'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('register/', RegisterView, name='register'),
]
