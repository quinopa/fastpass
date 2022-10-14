from django import forms
from django.core.exceptions import ValidationError

from . import models

class PasswordForm(forms.Form):
    name = forms.CharField(max_length=256)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)

    def clean_name(self):
        name = self.cleaned_data['name']
        if models.PasswordModel.objects.filter(name=name).exists():
            raise ValidationError("Entry already exists")
        return name