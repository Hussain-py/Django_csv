from django import forms
from .models import keyword_info
from django.forms import ModelForm

# creating a form
class InputForm(forms.Form):
    search_term = forms.CharField(max_length=200)
    # area = forms.CharField(max_length=200)
    # radius = forms.CharField(max_length=200)
    # typ = forms.CharField(max_length=200)

# class InputForm(forms.ModelForm):
#     search_term = forms.CharField(max_length=200)
#
#     class Meta:
#         model=data
#         fields=('title',)
