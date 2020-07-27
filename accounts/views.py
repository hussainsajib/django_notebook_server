from django.http import HttpResponse

# Create your views here.


def HomeView(request):
    return HttpResponse("Hello, World!")


def LoginView(request):
    return HttpResponse("Please login")


def LogoutView(request):
    return HttpResponse("You have been logged out")


def RegisterView(request):
    return HttpResponse("Please register")
