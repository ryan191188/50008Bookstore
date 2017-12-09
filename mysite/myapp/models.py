# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.conf import settings
#from django.contrib.auth import get_user_model
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#from django.contrib.auth.models import UserManager
# Create your models here.
# class CustomerManager(BaseUserManager):
#     def create_user(self,username,password, name):
#         user = self.model(
#             username = username,
#             name = name,
#             #password = password
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,username,password,name):
#         user = self.model(
#             username = username,
#             name = name,
#             #password = password
#         )
#         user.is_staff = True
#         user.is_superuser = True 
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=50, unique=True)
#     login = models.CharField(max_length=50, unique=True, primary_key=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = ['name','password']

#     objects = CustomerManager()

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=30)
#     login = models.CharField(max_length=50)
#     pw= models.CharField(max_length=60)
    

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     format = models.CharField(max_length=9)
#     pages = models.IntegerField(default=0)
#     languages = models.CharField(max_length=32)
#     authors = models.CharField(max_length=30)
#     publisher = models.CharField(max_length=30)
#     bookSubject =  models.CharField(max_length=30)
#     publication_date = models.DateField()
#     ISBN10 = models.CharField(max_length=20,default='')
#     ISBN13 = models.CharField(max_length=20, default='',primary_key=True)
#     numberOfCopies = models.IntegerField()


#ew_user=User.objects.create_user('xiexin2011@gmail.com', '1TJT599QE2','XIE XIN')