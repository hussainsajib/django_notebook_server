from django.urls import path, include

from .views import HomeView, SignupView, ProfileView, ProfileUpdateView

urlpatterns = [
    path('', HomeView, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/update/', ProfileUpdateView.as_view(), name='update_profile')
]
