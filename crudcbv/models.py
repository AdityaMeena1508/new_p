from django.db import models

# Create your models here.

gen = (
    ('male','male'),
    ('female','female'),
    ('other','other')
)

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(choices = gen, max_length=20)
