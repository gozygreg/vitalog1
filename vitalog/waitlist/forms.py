from django import forms
from .models import WaitlistUser

class WaitlistForm(forms.ModelForm):
    class Meta:
        model = WaitlistUser
        fields = ['name', 'email', 'phone_number', 'health_challenge', 'note']
