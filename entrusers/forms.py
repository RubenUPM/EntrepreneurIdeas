from django import forms
from .models import EntrepreneurUser


class EntrepreneurUserForm(forms.ModelForm):
    class Meta:
        model = EntrepreneurUser
        fields = ["name", "surname", "email", "password"]


class RawProductForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
