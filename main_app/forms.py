from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['is_teacher']
    labels = {
            'is_teacher': 'I Am A Teacher',
            
    }