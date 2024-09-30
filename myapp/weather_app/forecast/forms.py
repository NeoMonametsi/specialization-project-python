from django import forms
from .models import Feedback

class LocationForm(forms.Form):
    location = forms.CharField(label='Enter a city name', max_length=100)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']