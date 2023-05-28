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


#formulaire pour le serveur DHCP
class QuestionForm(forms.Form):
    question1 = forms.CharField(label='Adresse de réseau:', max_length=100)
    question2 = forms.CharField(label='masque de réseau:', max_length=100)
    question3 = forms.CharField(label='Début de la plage:', max_length=100)
    question4 = forms.CharField(label='Fin de la plage  :', max_length=100)
    question5 = forms.CharField(label='Passerelle:', max_length=100)
    question6 = forms.CharField(label='Serveur DNS:', max_length=100)
    question7 = forms.CharField(label='Adresse de diffusion:', max_length=100)

    # Ajoutez ici autant de champs de question que nécessaire
