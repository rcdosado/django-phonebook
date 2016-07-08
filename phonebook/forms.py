from django import forms
from . import models


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['first_name', 'last_name', 'email', 'address']