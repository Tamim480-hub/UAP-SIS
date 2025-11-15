path('exam-routine/', views.exam_routine, name='exam_routine'),
path('exam-routine/add/', views.add_exam_routine, name='add_exam_routine'),
path('exam-routine/<int:pk>/delete/', views.delete_exam_routine, name='delete_exam_routine'),
