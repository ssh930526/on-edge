from django.contrib import admin

# Register your models here.
from .models import Classroom, Assignment

admin.site.register(Classroom)
admin.site.register(Assignment)