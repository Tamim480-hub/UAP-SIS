from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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



class Routine(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    pdf = models.FileField(upload_to='routines/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Untitled Routine"

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=50, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

from django.db import models

class ExamRoutine(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='exam_routines/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

    class Meta:
        unique_together = ('student', 'date')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics/', default='default_profile.png')

    def __str__(self):
        return self.user.username


