from django.db import models

class Book(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    year=models.IntegerField()
# Create your models here.

