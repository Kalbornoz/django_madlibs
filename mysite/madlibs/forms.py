from django import forms
from .models import FillIns
from django.forms import TextInput


class FillInsForm(forms.ModelForm):
    class Meta:
        model = FillIns
        fields = ['field1', 'field2', 'field3',
                  'field4', 'field5', 'field6', 'field7']
        widgets = {
            'field1': TextInput(attrs={
                'class': "form-control",
            }),
            'field2': TextInput(attrs={
                'class': "form-control",
            }),
            'field3': TextInput(attrs={
                'class': "form-control",
            }),
            'field4': TextInput(attrs={
                'class': "form-control",
            }),
            'field5': TextInput(attrs={
                'class': "form-control",
            }),
            'field6': TextInput(attrs={
                'class': "form-control",
            }),
            'field7': TextInput(attrs={
                'class': "form-control",
            }),
        }
