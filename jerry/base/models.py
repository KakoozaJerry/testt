from django.db import models
from datetime import date, datetime

class Employees(models.Model):
    employee_id = models.IntegerField()
    date = models.DateField()
    seniority = models.CharField(max_length=30)

class Points(models.Model):
    employeepoints_id = models.IntegerField()
    pointsattained = models.CharField(max_length=30)
    tenure = models.CharField(max_length=30, default='0')
    seniority = models.CharField(max_length=30, default='A')
    passwordz = models.CharField(max_length=30, default = '123')





