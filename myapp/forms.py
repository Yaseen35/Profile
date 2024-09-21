from django import forms
from .models import UserProfile  # Import the Profile model

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Specify the model
        fields = ['full_name','email','address','state','education','experience','country','profile_image']
