from django.db import models

class Student(models.Model):
    registration = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    father_name = models.CharField(max_length=200, default="Not Provided")
    mother_name = models.CharField(max_length=200, default="Not Provided")
    address = models.CharField(max_length=255, default="Not Provided")
    phone = models.CharField(max_length=20, blank=True, default="")
    gender = models.CharField(max_length=10, default='Male')
    blood_group = models.CharField(max_length=5, blank=True, default="")
    BoD = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.registration} - {self.name}"



