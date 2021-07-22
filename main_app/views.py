from django.shortcuts import render
from .models import Assignment
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

class AssignmentList(LoginRequiredMixin, ListView):
    model = Assignment

class AssignmenDetail(LoginRequiredMixin, DetailView ):
    model = Assignment