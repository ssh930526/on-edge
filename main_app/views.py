from django.shortcuts import render, redirect
from .models import Assignment, Classroom, Student
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
    unassigned_assignments = assignments.exclude(id__in = classroom.assignments.all().values_list('id'))
    return render(req, 'classrooms/detail.html', {
        'classroom': classroom,
        'allAssignments': assignments,
        'unassigned': unassigned_assignments
    })

@login_required
def assoc_assignment_to_classroom(req, classroom_id, assignment_id):
    Classroom.objects.get(id=classroom_id).assignments.add(assignment_id)
    return redirect('classrooms_detail', classroom_id=classroom_id)

@login_required
def unassoc_assignment_to_classroom(req, classroom_id, assignment_id):
    Classroom.objects.get(id=classroom_id).assignments.remove(assignment_id)
    return redirect('classrooms_detail', classroom_id=classroom_id)

class ClassroomCreate(LoginRequiredMixin, CreateView):
    model = Classroom
    fields = ['course_subject', 'course_number', 'course_name']
    success_url = '/classrooms/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ClassroomUpdate(LoginRequiredMixin, UpdateView):
    model = Classroom
    fields = ['course_subject', 'course_number', 'course_name']
    success_url = '/classrooms/'

class ClassroomDelete(LoginRequiredMixin, DeleteView):
    model = Classroom
    success_url = '/classrooms/'



def signup(request):
    error_message = ''
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
        else:
            error_message = 'Invalid Signup Data - Please Try Again'
    #create user
    user_form = UserCreationForm()
    profile_form = ProfileForm()

    return render(request, 'registration/signup.html', {
        'user_form': user_form, 
        'error_message': error_message,
        'profile_form': profile_form 
    })
    # return render(request, 'registration/signup.html', context)
   

def dashboard_index(req):
    assignments = Assignment.objects.filter(user=req.user)
    classrooms = Classroom.objects.filter(user=req.user)
    return render(req, 'dashboard.html', {
        'assignments': assignments,
        'classrooms': classrooms,
        'user': req.user
    })
  
@login_required  
def students_index(req):
    students = Student.objects.all()
    return render(req, 'students/index.html', {'students': students})

@login_required
def students_detail(req, student_id):
    student = Student.objects.get(id=student_id)
    return render(req, 'students/detail.html', {'student': student})

class StudentsCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'
    success_url = '/students/'

class StudentsUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/students/'

class StudentsDelete(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = '/students/'
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    context = {
    'user_form': user_form, 
    'profile_form': profile_form
  }

@login_required
def dashboard(request):
  user_type = None
  if request.user.profile.is_teacher:
    user_type = 'teacher'
  else:
    user_type = 'student'
  return render(request, f'{user_type}_dashboard.html')