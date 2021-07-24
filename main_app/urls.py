from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Routes for Classrooms
    path('classrooms/', views.classrooms_index, name='classrooms_index'),
    path('classrooms/<int:classroom_id>/', views.classrooms_detail, name='classrooms_detail'),
    path('classrooms/create/', views.ClassroomCreate.as_view(), name='classrooms_create'),
    path('classrooms/<int:pk>/update/', views.ClassroomUpdate.as_view(), name='classrooms_update'),
    path('classrooms/<int:pk>/delete/', views.ClassroomDelete.as_view(), name='classrooms_delete'),
    # Routes for Assignments
    path('assignments/', views.AssignmentList.as_view(), name='assignments_index'),
    path('assignments/<int:pk>/', views.AssignmenDetail.as_view(), name='assignments_detail'),
    path('assignments/create/', views.AssignmentCreate.as_view(), name='assignments_create'),
    path('assignments/<int:pk>/update', views.AssignmentUpdate.as_view(), name='assignments_update'),
    path('assignments/<int:pk>/delete', views.AssignmentDelete.as_view(), name='assignments_delete'),
]