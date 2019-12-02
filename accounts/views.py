from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel

from accounts.forms import UserForm
# Create your views here.

class SignUp(CreateView):
    
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    
    