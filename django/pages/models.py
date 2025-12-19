from django.db import models

# Create your models here.
class Instance(models.Model):
    address = models.CharField(max_length=200, unique=True)