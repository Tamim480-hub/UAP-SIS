from django import forms
from .models import Teacher

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