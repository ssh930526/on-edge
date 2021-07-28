from django.shortcuts import render, redirect
from .models import Assignment, Classroom
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

class AssignmentList(LoginRequiredMixin, ListView):
    model = Assignment

class AssignmenDetail(LoginRequiredMixin, DetailView ):
    model = Assignment

class AssignmentCreate(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['description', 'due_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class AssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assignment
    fields = ['description', 'due_date']

class AssignmentDelete(LoginRequiredMixin,DeleteView):
    model = Assignment
    success_url = '/assignments/'

@login_required  
def classrooms_index(req):
    classrooms = Classroom.objects.all()
    return render(req, 'classrooms/index.html', {'classrooms': classrooms})

@login_required
def classrooms_detail(req, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    return render(req, 'classrooms/detail.html', {'classroom': classroom})
    
class ClassroomCreate(LoginRequiredMixin, CreateView):
    model = Classroom
    fields = '__all__'
    success_url = '/classrooms/'

class ClassroomUpdate(LoginRequiredMixin, UpdateView):
    model = Classroom
    fields = '__all__'
    success_url = '/classrooms/'


class ClassroomDelete(LoginRequiredMixin, DeleteView):
    model = Classroom
    success_url = '/classrooms/'



def signup(request):
    # error_message = ''
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('classrooms_index')
        # else:
        #     error_message = 'Invalid Signup Data - Please Try Again'


    #create user
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    context = {
    'user_form': user_form, 
    'profile_form': profile_form
  }
   

    return render(request, 'registration/signup.html', context)
   

@login_required
def dashboard(request):
  user_type = None
  if request.user.profile.is_teacher:
    user_type = 'teacher'
  else:
    user_type = 'student'
  return render(request, f'{user_type}_dashboard.html')








    
