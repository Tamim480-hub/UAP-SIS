from django.urls import path
from . import views

urlpatterns=[

    path('home/', views.home_views, name='home'),
    path('home/dashboard.html/', views.dashboard, name='dashboard.html'),
    path('login/', views.login_views, name='login'),
    path('search/', views.search_views, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/dashboard/attendance/', views.attendance_views, name='attendance'),
    path('routine/', views.routine, name='routine'),
]