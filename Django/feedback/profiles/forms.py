from django import forms

class ProfileForm(forms.Form):
    user_pdf = forms.FileField()