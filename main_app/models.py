from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=CASCADE)
    

class Assignment(models.Model):
    description = models.TextField(max_length=1000)
    due_date = models.DateField()
    completeted_date = models.DateField() 
    teacher = models.ForeignKey(User, on_delete=CASCADE)

class Classroom(models.Model):
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(User, on_delete=CASCADE)

