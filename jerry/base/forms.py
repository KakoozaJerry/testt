from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    passwor_d = forms.CharField(label='Password', max_length=100)