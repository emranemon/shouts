from django.contrib import admin

from django.urls import path, include
from accounts import views

urlpatterns = [
    path('user/', include('django.contrib.auth.urls')), # for authentications login/logout 
    path('user/signup/', views.SignUp.as_view(), name='signup'),
    

    
]