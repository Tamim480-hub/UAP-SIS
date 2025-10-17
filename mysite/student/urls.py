from django.urls import path
from . import views
app_name = 'student'

urlpatterns=[

    path('home/', views.home_views, name='home'),
    path('home/dashboard.html/', views.dashboard, name='dashboard.html'),
    path('login/', views.login_views, name='login'),
    path('search/', views.search_views, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/dashboard/attendance/', views.attendance_views, name='attendance'),
    path('routine/', views.routine, name='routine'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/<int:pk>/edit/', views.edit_teacher, name='teacher_edit'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),

]
