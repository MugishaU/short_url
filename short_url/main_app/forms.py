from django import forms
from django.forms import ModelForm

from .models import *

class UrlForm(forms.ModelForm):
    
    class Meta:
        model = Urls
        fields = ['long_url']