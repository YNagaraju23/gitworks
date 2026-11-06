from django.db import models
class Book(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    year=models.IntegerField()
    def __str__(self):
        return self.author
class Student(models.Model):
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=40)
    standard=models.IntegerField()
    def __str__(self):
        return self.name
# Create your models here.
