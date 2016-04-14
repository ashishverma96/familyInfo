from django import forms

# our new form


class InfoForm(forms.Form):
    name = forms.CharField(required=True)
    year = forms.IntegerField(required=True)