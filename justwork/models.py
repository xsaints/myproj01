from django.db import models
from django.urls import reverse

from django.conf import settings

import datetime


class Demo(models.Model):
    name = models.CharField(max_length= 10, null=False, blank=False)

    def __str__(self):
        return self.name


class Department(models.Model):
    department_id = models.IntegerField(blank= False, null= False, unique= True)
    department_name = models.CharField(max_length=30, null = False, blank= False, unique= True)
    manager_id  = models.IntegerField()
    location_id = models.IntegerField()

    def __str__(self):
        return self.department_name
        
        
class Employee(models.Model):
    employee_id  = models.IntegerField(null= False, blank=False, unique= True)
    entry_date= models.DateTimeField(auto_now_add= True)
    last_update= models.DateTimeField(auto_now= True)
    first_name   = models.CharField(max_length=20, null = False, blank= False)
    last_name    = models.CharField(max_length=25, null = False, blank= False)
    email        = models.CharField(max_length=25) 
    phone_number = models.CharField(max_length=20)
    hire_date    = models.DateField()
    job_id       = models.CharField(max_length=10)
    salary       = models.DecimalField(max_digits=10, decimal_places=2)
    commission_pct=models.DecimalField(max_digits= 4, decimal_places=2)
    manager_id   = models.IntegerField()
    department_id= models.ForeignKey(Department, on_delete= models.CASCADE)	    

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.hire_date.strftime("%Y-%m-%d")
