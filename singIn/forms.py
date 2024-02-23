from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class Singupforms(UserCreationForm):
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name', 'email']

class EdituserProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']
        label = {"email" : "Email"}

class EditadminProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        label = {"email" : "Email"}
        

