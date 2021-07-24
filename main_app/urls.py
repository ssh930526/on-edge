from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('classrooms/', views.classrooms_index, name='classrooms_index'),
    path('classrooms/<int:classroom_id>/', views.classrooms_detail, name='classrooms_detail'),
    path('classrooms/create/', views.ClassroomCreate.as_view(), name='classrooms_create'),
    path('classrooms/<int:pk>/update/', views.ClassroomUpdate.as_view(), name='classrooms_update'),
    path('classrooms/<int:pk>/delete/', views.ClassroomDelete.as_view(), name='classrooms_delete'),

]