from django.contrib import admin
from .models import Student, Routine


admin.site.register(Student)


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'teacher_name', 'day', 'start_time', 'end_time', 'room_no')
    list_filter = ('day', 'teacher_name')
