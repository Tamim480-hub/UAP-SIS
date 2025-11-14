from datetime import timezone
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from .forms import CustomUserCreationForm, CustomAuthenticationForm, ExamRoutineForm, ProfileForm
from .forms import RoutineForm
from .models import Attendance
from .models import Student, Teacher, Routine, ExamRoutine, Profile


# ------------------ LOGIN ------------------
def signin_views(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.email}!")
            # Dashboard URL with namespace
            return redirect("student:dashboard")
    else:
        form = CustomAuthenticationForm()
    return render(request, "student/signin.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # assign username (optional) and first_name / last_name
            user.username = f"{form.cleaned_data['first_name']}_{form.cleaned_data['last_name']}".lower()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("student:signin")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "student/signup.html", {"form": form})


# ------------------ DASHBOARD ------------------
@login_required(login_url='signin_views')
def dashboard(request):
    return render(request, "student/dashboard.html")


# ------------------ LOGOUT ------------------
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("student:signin")


# ------------------ OTHER VIEWS ------------------
def search_views(request):
    query = request.GET.get('q', '').strip()
    students = Student.objects.none()
    if query:
        students = Student.objects.filter(
            Q(registration__icontains=query) | Q(name__icontains=query)
        )
    return render(request, 'student/search.html', {'students': students, 'query': query})



def attendance(request):
    students = Student.objects.all()  # সব student list

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        status_value = request.POST.get('attendance_1')
        date_instance = timezone.now().date()  # আজকের তারিখ

        student_instance = Student.objects.filter(id=student_id).first()
        if not student_instance:
            return render(request, 'student/attendance.html', {
                'students': students,
                'error': 'Student not found'
            })

        # Attendance update_or_create
        Attendance.objects.update_or_create(
            student=student_instance,
            date=date_instance,
            defaults={'status': status_value}
        )

        return render(request, 'student/attendance.html', {
            'students': students,
            'success': 'Attendance updated!'
        })

    return render(request, 'student/attendance.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'student/teacher.html', {'teachers': teachers})


def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        hire_date = request.POST.get('hire_date')
        photo = request.FILES.get('photo')

        if Teacher.objects.filter(email=email).exists():
            messages.error(request, 'A teacher with this email already exists!')
        else:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                department=department,
                hire_date=hire_date,
                photo=photo
            )
            messages.success(request, 'Teacher added successfully!')

        return redirect('student:add_teacher')

    teachers = Teacher.objects.all()
    return render(request, 'student/teacher.html', {'teachers': teachers})


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    fields = [
        {'name': field.verbose_name.capitalize(), 'value': getattr(teacher, field.name)}
        for field in teacher._meta.fields if field.name != "id"
    ]
    return render(request, 'student/teacher_detail.html', {'teacher': teacher, 'fields': fields})


def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.email = request.POST.get('email')
        teacher.department = request.POST.get('department')
        teacher.hire_date = request.POST.get('hire_date')
        if request.FILES.get('photo'):
            teacher.photo = request.FILES.get('photo')
        teacher.save()
        return redirect('student:teacher_list')  # Teacher list page


    return render(request, 'student/teacher_edit.html', {'teacher': teacher})


def teacher_delete(pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('student:teacher_list')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'student/login.html', {'form': form})



@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture updated successfully!')
            return redirect('student:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'student/profile.html', {'form': form, 'profile': profile})



def routine_view(request):
    routines_list = Routine.objects.all().order_by('-uploaded_at')
    form = RoutineForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('student:routine')  # URL name must match urls.py

    context = {
        'form': form,
        'routines': routines_list,
    }
    return render(request, 'student/routine.html', context)


def delete_routine(request, pk):
    routine_item = get_object_or_404(Routine, pk=pk)
    if request.method == 'POST':
        routine_item.delete()
    return redirect('student:routine')


def exam_routine(request):
    routines = ExamRoutine.objects.all()
    if request.method == 'POST':
        form = ExamRoutineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student:exam_routine')
    else:
        form = ExamRoutineForm()

    context = {
        'form': form,
        'routines': routines
    }
    return render(request, 'student/exam_routine.html', context)

# Add new routine
def add_exam_routine(request):
    if request.method == 'POST':
        form = ExamRoutineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student:exam_routine_list')
    else:
        form = ExamRoutineForm()
    return render(request, 'student/add_exam_routine.html', {'form': form})

# Delete routine
def delete_exam_routine(request, pk):
    routine = get_object_or_404(ExamRoutine, pk=pk)
    if request.method == "POST":
        routine.delete()
        return redirect('student:exam_routine')  # redirect to exam routine list
    return redirect('student:exam_routine')

