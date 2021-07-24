from django.shortcuts import render, redirect
from .models import Assignment, Classroom
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')


class AssignmentList(ListView):
    model = Assignment

class AssignmenDetail(DetailView ):
    model = Assignment

class AssignmentCreate(CreateView):
    model = Assignment
    fields = ['description', 'due_date']

class AssignmentUpdate(UpdateView):
    model = Assignment
    fields = ['description', 'due_date']

class AssignmentDelete(DeleteView):
    model = Assignment
    success_url = '/assignments/'
    
def classrooms_index(req):
    classrooms = Classroom.objects.all()
    return render(req, 'classrooms/index.html', {'classrooms': classrooms})

def classrooms_detail(req, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    return render(req, 'classrooms/detail.html', {'classroom': classroom})
    
class ClassroomCreate(CreateView):
    model = Classroom
    fields = '__all__'
    success_url = '/classrooms/'

class ClassroomUpdate(UpdateView):
    model = Classroom
    fields = '__all__'

class ClassroomDelete(DeleteView):
    model = Classroom
    success_url = '/classrooms/'

