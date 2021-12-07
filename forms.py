from django import forms
from .models import User
from django.forms import widgets

#THIS IS FORM GO TO VIEWS

class Student(forms.ModelForm):
   class Meta:
      model=User
      fields=['name','email','password']
      widgets={ 'name':forms.TextInput(attrs={'class':'form-control'}),
       'email':forms.EmailInput(attrs={'class':'form-control'}),
       'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
         }