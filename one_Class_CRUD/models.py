from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20)
    eid = models.IntegerField()
    eage = models.IntegerField()

    
