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

@login_required  
def assignments_index(req):
    assignments = Assignment.objects.filter(user=req.user)
    return render(req, 'assignments/index.html', {'assignments': assignments})

@login_required  
def assignments_detail(req, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    return render(req, 'assignments/detail.html', {'assignment': assignment})
    
class AssignmentCreate(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['description', 'due_date']
    success_url = '/assignments/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class AssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assignment
    fields = ['description', 'due_date']
    success_url = '/assignments/'

class AssignmentDelete(LoginRequiredMixin,DeleteView):
    model = Assignment
    success_url = '/assignments/'

@login_required  
def classrooms_index(req):
    classrooms = Classroom.objects.filter(user=req.user)
    return render(req, 'classrooms/index.html', {'classrooms': classrooms})

@login_required  
def classrooms_detail(req, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    assignments = Assignment.objects.filter(user=req.user)
    return render(req, 'classrooms/detail.html', {
        'classroom': classroom,
        'assignments': assignments
    })
    
class ClassroomCreate(LoginRequiredMixin, CreateView):
    model = Classroom
    fields = ['course_subject', 'course_number', 'course_name']
    success_url = '/classrooms/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ClassroomUpdate(LoginRequiredMixin, UpdateView):
    model = Classroom
    fields = '__all__'
    success_url = '/classrooms/'

class ClassroomDelete(LoginRequiredMixin, DeleteView):
    model = Classroom
    success_url = '/classrooms/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('classrooms_index')
        else:
            error_message = 'Invalid Signup Data - Please Try Again'


    #create user
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message })
  
    
def dashboard_index(req):
    assignments = Assignment.objects.filter(user=req.user)
    classrooms = Classroom.objects.filter(user=req.user)
    return render(req, 'dashboard.html', {
        'assignments': assignments,
        'classrooms': classrooms,
        'user': req.user
    })