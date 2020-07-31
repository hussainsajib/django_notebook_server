from django.shortcuts import render

# Create your views here.


def HomeView(request):
    return render(request, 'home.html')


def LoginView(request):
    return HttpResponse("Please login")


def LogoutView(request):
    return HttpResponse("You have been logged out")


def RegisterView(request):
    return HttpResponse("Please register")
