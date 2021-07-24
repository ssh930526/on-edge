from django.shortcuts import render, redirect
from .models import Assignment, Classroom
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Signup Data - Please Try Again'


    #create user
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message })
  
    
