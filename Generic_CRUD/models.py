from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    sid = models.IntegerField()

    def __str__(self) -> str:
        return self.name, self.subject