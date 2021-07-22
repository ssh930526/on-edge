from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Student model 
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.first_name
    

class Assignment(models.Model):
    description = models.TextField(max_length=1000)
    due_date = models.DateField()
    completed_date = models.DateField() 
    teacher = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.first_name


class Classroom(models.Model):
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(User, on_delete=CASCADE)

