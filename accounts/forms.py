from django import forms
from accounts.models import UserModel
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta():
        model = UserModel
        fields = UserCreationForm.Meta.fields + ('portfolio_site','first_name','last_name','email','profile_pic')
        
    
        
    