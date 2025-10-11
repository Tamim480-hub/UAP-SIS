from django.db import models


class ExamRoutine(models.Model):
    exam_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=50)
    room_no = models.CharField(max_length=20)

    def _str_(self):
        return f"{self.exam_name} - {self.course_name}"