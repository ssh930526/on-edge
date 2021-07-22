from django.shortcuts import render
from .models import Assignment
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