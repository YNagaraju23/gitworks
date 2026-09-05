from django.db import models
class createTable(models.Model):
    name=models.CharField(max_length=20)
    sno=models.IntegerField()
    def __str__(self):
        return f" {{self.name}} and sno is {{self.sno}}"
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=60)
# Create your models here.
