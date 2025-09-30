from django.shortcuts import render


# Home Page View
def home_views(request):
    return render(request, "home.html")


# Log In Page View
def login_views(request):
    return render(request, "auth/login.html")


# Sign Up Page View
def dashboard(request):
    return render(request, "auth/dashboard.html")