from django import forms
from .models import Customer
class CustomerForm(forms.Form):
    full_name=forms.CharField(label='Full Name',max_length=30,error_messages={
      'required':'your name cant be empty'  ,
      'max:length':'extedns limit',
    })
    email=forms.CharField(label='Email',max_length=30,error_messages={
        'required':'your email cant be left empty',
        'max_length':'exceeds length'
    })