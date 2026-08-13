from django import forms
class Inputform(forms.Form):
    surname=forms.CharField(max_length=10)
    name = forms.CharField(max_length=20)