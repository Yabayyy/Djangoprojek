from django.db import models

# Create your models here.
class Costumer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=264, unique=True)