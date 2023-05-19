from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render


class AddMachineForm(forms.Form) :
    
    nom = forms.CharField(required=True, label='Nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 10 :
            
            return 'computerApp/machine_add.html'
           
        return data

class AddPersonneForm(forms.Form) :
    
    nom = forms.CharField(required=True, label='Nom du Personnel')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 10 :
            
            return 'computerApp/machine_add.html'
           
        return data