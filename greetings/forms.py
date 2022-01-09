from django import forms

class GreetingForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)