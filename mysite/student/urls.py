from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name = 'student'

urlpatterns=[

    path('signin/', views.signin_views, name='signin'),
    path('signin/dashboard.html/', views.dashboard, name='dashboard.html'),
    path('student/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('search/', views.search_views, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("attendance/", views.attendance, name="attendance"),
    path('routine/', views.routine_view, name='routine'),
    path('routine/delete/<int:pk>/', views.delete_routine, name='delete_routine'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/<int:pk>/edit/', views.edit_teacher, name='edit_teacher'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('student/logout/', auth_views.LogoutView.as_view(next_page='student:login'), name='logout'),
    path('student/profile/', views.profile, name='profile'),
    path('exam-routine/', views.exam_routine, name='exam_routine'),
    path('exam_routine/add/', views.add_exam_routine, name='add_exam_routine'),
    path('exam_routine/<int:pk>/delete/', views.delete_exam_routine, name='delete_exam_routine'),
    path("logout/", views.logout_view, name="logout"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)