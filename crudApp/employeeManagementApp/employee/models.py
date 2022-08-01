from django.db import models
import datetime


# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    dob = models.CharField(max_length=50)
    email = models.EmailField()
    contactNumber = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    department = models.CharField(max_length=50,default=None, null=True)
    education = models.CharField(max_length = 20, default=None, null=True)
    joiningDate = models.CharField(max_length = 20, default=None, null=True)


class Meta:
    db_table = "employee"
