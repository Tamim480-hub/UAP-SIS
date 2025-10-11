from django.contrib import admin
from .models import ExamRoutine

@admin.register(ExamRoutine)
class ExamRoutineAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'course_name', 'date', 'time', 'room_no')