from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser, ExamRoutine
from .models import Routine
from .models import Teacher
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class TeacherForm(forms.ModelForm):
     class Meta:
            model = Teacher
            fields = '__all__'
            widgets = {
                'hire_date': forms.DateInput(attrs={'type': 'date'})
            }



class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))



class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['title', 'pdf']

class ExamRoutineForm(forms.ModelForm):
    class Meta:
        model = ExamRoutine
        fields = ['title', 'pdf_file']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']

