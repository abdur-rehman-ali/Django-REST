from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField()
    faculty = models.CharField(max_length=20)

    