# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=50)
    pw= models.CharField(max_length=60)


class Book(models.Model):
    title = models.CharField(max_length=100)
    format = models.CharField(max_length=9)
    pages = models.IntegerField(default=0)
    languages = models.CharField(32)
    authors = models.ManyToManyField(Author)
    #publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()