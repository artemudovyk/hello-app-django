from django import forms

class GreetingForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=40)