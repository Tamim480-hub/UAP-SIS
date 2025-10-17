from django.contrib import admin
from .models import Student, Routine, Teacher

admin.site.register(Student)


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'teacher_name', 'day', 'start_time', 'end_time', 'room_no')
    list_filter = ('day', 'teacher_name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'department', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    list_filter = ('department', )
    ordering = ('id',)