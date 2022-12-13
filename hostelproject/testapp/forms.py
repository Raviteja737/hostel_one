from django import forms
from django.contrib.auth.models import User
from testapp.models import Register
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'
