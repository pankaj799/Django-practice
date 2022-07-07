from django import forms

from .models import Participant

class RegistreationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']