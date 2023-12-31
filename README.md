# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 students

## PROGRAM
'''
admin.py

from django.contrib import admin
from .models import students,studentsAdmin
admin.site.register(students,studentsAdmin)


models.py

from django.db import models

from django.contrib import admin
class students (models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=100,default=00000)
    age=models.IntegerField()
    mobileno=models.IntegerField()
    city=models.CharField(max_length=100,default=0000)

class studentsAdmin(admin.ModelAdmin):
    list_display=('rollno','name','age','mobileno','city')
'''
## OUTPUT

![output_1](https://github.com/dinesh2068/ORM/assets/151390189/f1e6788f-b388-41c3-8f1e-27de90624308)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
