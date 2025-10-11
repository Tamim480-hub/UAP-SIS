from django.shortcuts import render
from .models import ExamRoutine

def exam_routine_view(request):
    routines = ExamRoutine.objects.all().order_by('date', 'time')
    return render(request, 'exam/exam_routine.html', {'routines': routines})