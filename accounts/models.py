from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class UserModel(User):

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)