from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model


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

    def get_queryset(self):
        return get_user_model().objects.filter(username=self.request.user).get()
