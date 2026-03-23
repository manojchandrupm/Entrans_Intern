from django.db import models

# Create your models here.

# class Product(models.Model):
#     Product_name = models.CharField(max_length=50,null=True)
#     Product_code = models.CharField(max_length=10,null=True)
#     Price = models.IntegerField(default=0)
#     gst = models.IntegerField(default=0)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
