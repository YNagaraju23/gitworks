from django.db import models
class createTable(models.Model):
    name=models.CharField(max_length=20)
    sno=models.IntegerField()
    def __str__(self):
        return self.name
# Create your models here.
