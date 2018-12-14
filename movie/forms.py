from django import forms
from django.contrib.auth.models import User
from movie.models import Customer

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        
        model=User
        fields=('first_name','last_name','username','password','email')

class RegistrationForm(forms.ModelForm):
    
    class Meta():
        
        model=Customer
        fields=('gender','contact','states','city')