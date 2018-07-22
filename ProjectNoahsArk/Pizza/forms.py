from django import forms

class InputForm(forms.Form):
    Pizza1_r=forms.FloatField(label="Pizza#1 Radius: ",initial=0.0)
    Pizza1_h=forms.FloatField(label="Pizza#1 Height: ",initial=0.0)
    Pizza1_p=forms.FloatField(label="Pizza#1 Price: ",initial=1.0)
    Pizza2_r=forms.FloatField(label="Pizza#2 Radius: ",initial=0.0)
    Pizza2_h=forms.FloatField(label="Pizza#2 Height: ",initial=0.0)
    Pizza2_p=forms.FloatField(label="Pizza#2 Price: ",initial=1.0)