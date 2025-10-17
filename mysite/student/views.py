from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Student, Routine
from .models import Teacher


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
    students = Student.objects.none()  

    if query:

        students = Student.objects.filter(
            Q(registration__icontains=query) | Q(name__icontains=query)
        )

    return render(request, 'student/search.html', {'students': students, 'query': query})




def attendance_views(request):

    return render(request, "student/attendance.html", )

def routine(request):
    routines = Routine.objects.all().order_by('day', 'start_time')
    return render(request, 'student/routine.html', {'routines': routines})



def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'student/teacher.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST.get('last_name', '')
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        department = request.POST.get('department', '')
        hire_date = request.POST.get('hire_date', None)  
        photo = request.FILES.get('photo', None)  

        Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            department=department,
            hire_date=hire_date,
            photo=photo
        )
        return redirect('student:teacher_list')
    return render(request, 'student/add_teacher.html')


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

  
    fields = []
    for field in teacher._meta.fields:
        if field.name != "id":
            fields.append({
                'name': field.verbose_name.capitalize(),
                'value': getattr(teacher, field.name)
            })

    return render(request, 'student/teacher_detail.html', {
        'teacher': teacher,
        'fields': fields
    })

def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.name = request.POST['name']
        teacher.department = request.POST['department']
        teacher.email = request.POST['email']
        teacher.phone = request.POST['phone']
        teacher.save()
        return redirect('teacher_list')
    return render(request, 'student/edit_teacher.html', {'teacher': teacher})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('student:teacher_list')
