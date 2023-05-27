from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Machine


class AddMachineForm(forms.Form) :
    
    nom = forms.CharField(required=True, label='Nom de la machine')
    IP = forms.GenericIPAddressField(required=True, label='IP de la machine')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        
        if len(data) > 10 :
            raise ValidationError('erreur de champ')
        return data                                             
    def clean_IP(self):
        data = self.cleaned_data["IP"]
        
        if len(data) > 15 :
            raise ValidationError('erreur de champ')
        return data

class AddPersonneForm(forms.Form) :
    
    nom = forms.CharField(required=True, label='Nom du Personnel')
    socialsecurity = forms.CharField(required=True, label='Numéro de sécu')
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 10 :
            raise ValidationError('erreur de champ')
        return data
    def clean_socialsecurity(self):
        data = self.cleaned_data["socialsecurity"]
        if len(data) > 13 :
            raise ValidationError('erreur de champ')
        return data

class DelMachineForm(forms.Form) :
    selected_machine = forms.ModelMultipleChoiceField(
        queryset=Machine.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )



class QuestionForm(forms.Form):
    question1 = forms.CharField(label='Question fg', max_length=100)
    question2 = forms.CharField(label='Question 2', max_length=100)
    # Ajoutez ici autant de champs de question que nécessaire
