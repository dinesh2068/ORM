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