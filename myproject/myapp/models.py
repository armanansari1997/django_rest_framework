from django.db import models

# Create your models here.

class Employee(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
