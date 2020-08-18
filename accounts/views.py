from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import UserForm


def HomeView(request):
    return render(request, 'home.html')


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileView(TemplateView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'user_profile.html'

    def get_object(self):
        return get_user_model().objects.get(username=self.request.user)


class ProfileUpdateView(UpdateView):
    form_class = UserForm
    success_url = reverse_lazy('profile')
    template_name = 'update_user.html'

    def get_object(self):
        return self.request.user
