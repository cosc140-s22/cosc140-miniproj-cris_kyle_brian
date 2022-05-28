from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ['stars','review']

class AnswerForm(forms.Form):
  answer1 = forms.BooleanField()
  answer2 = forms.BooleanField()
  answer3 = forms.BooleanField()
  answer4 = forms.BooleanField()
  
