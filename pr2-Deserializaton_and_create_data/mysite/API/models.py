from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=200)
    reg_no = models.IntegerField()
    faculty = models.CharField(max_length=50)