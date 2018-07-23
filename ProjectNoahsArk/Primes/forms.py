from django import forms

class InputForm(forms.Form):
    Primelimit=forms.IntegerField(label="Max limit below which you want to get all prime numbers: ",initial=2)