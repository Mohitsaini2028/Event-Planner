# from django.forms import ModelForm
from django import forms
from .models import Event

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=255,widget= forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Event Name'}))
    data = forms.CharField(max_length=500,widget= forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter data here'}))
    location=forms.CharField(max_length=255,widget= forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Event Location '}))
    time = forms.TimeField(widget = forms.TextInput(attrs={'type':'time'}))
    img = forms.ImageField()
