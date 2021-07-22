from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Routes for Assignments
    path('assignments/', views.AssignmentList.as_view(), name='assignments_index'),
]