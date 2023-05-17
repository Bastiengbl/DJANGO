from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render


class AddMachineForm(forms.Form) :
    
    nom = forms.CharField(required=True, label='Nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 10 :
            return 'computerApp/error.html'
            print(forms.error)
        return data