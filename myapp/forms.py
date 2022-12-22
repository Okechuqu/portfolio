from django import forms
from django.forms import ModelForm
from .models import contact


class contactForm(ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-1', 'placeholder': 'Name/Company'}))

    address = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-2', 'placeholder': 'Address'}))

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control-3', 'placeholder': 'Email'}))

    phone = forms.IntegerField(label='', widget=forms.NumberInput(
        attrs={'class': 'form-control-4', 'placeholder': 'Phone Number'}))

    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control-5', 'placeholder': 'Job Description (specify skill in need)'}))

    class Meta:
        model = contact
        fields = 'name', 'address', 'email', 'phone', 'description'
