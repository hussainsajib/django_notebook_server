from django.urls import path, include

from .views import HomeView, SignupView, ProfileView

urlpatterns = [
    path('', HomeView, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]
