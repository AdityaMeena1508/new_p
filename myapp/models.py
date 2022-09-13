
from django.db import models

import uuid

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=200, primary_key=True)
    last_name = models.CharField(max_length=200, default=True)
    # def __repr__(self):
        
    #     return self.first_name , self.last_name
