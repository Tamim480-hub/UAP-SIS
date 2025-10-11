from django.urls import path
from . import views

urlpatterns = [
    path('exam-routine/', views.exam_routine_view, name='exam_routine'),
]