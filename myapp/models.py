from django.db import models

# import uuid

# Create your models here.
class myapp(models.Model):
    # name_id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    course = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.name