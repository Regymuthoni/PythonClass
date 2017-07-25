from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.TextField(max_length=100)
    course = models.CharField(max_length=50)
    description=models.TextField(default='Good student')
    
    
    

