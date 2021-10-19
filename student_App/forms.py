from django import forms
from .models import groupProjects

class groupProjectsForm(forms.ModelForm):
    class Meta:
        model = groupProjects
        fields = '__all__'