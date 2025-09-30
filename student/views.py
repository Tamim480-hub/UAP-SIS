from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Student


def home_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # start session
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "student/home.html")



def dashboard(request):
    return render(request, "student/dashboard.html")



def login_views(request):
    return  render(request, "student/login.html")

def search_views(request):
    query = request.GET.get('q', '').strip()
    students = Student.objects.none()  # default empty QuerySet

    if query:

        students = Student.objects.filter(
            Q(registration__icontains=query) | Q(name__icontains=query)
        )

    return render(request, 'student/search.html', {'students': students, 'query': query})




def attendance_views(request):

    return render(request, "student/attendance.html", )

def routine(request):

    return render(request, "student/routine.html", )

