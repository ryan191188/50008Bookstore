from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=50)
    pw= models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    format = models.CharField(max_length=9)
    pages = models.DateField()
    languages = models.CharField(32)
    authors = models.ManyToManyField(Author)
    #publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
