from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['is_teacher', 'first_name', 'last_name', 'email']
    labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'is_teacher': ''
    }