from django.contrib import admin
from .models import Student, Routine, Teacher

admin.site.register(Student)


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'department', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    list_filter = ('department',)