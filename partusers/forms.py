from django import forms
from .models import PartnerUser


class PartnerUserForm(forms.ModelForm):
    class Meta:
        model = PartnerUser
        fields = ["name", "surname", "email", "password"]


class RawProductForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
