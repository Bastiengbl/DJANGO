from django.shortcuts import render, redirect, get_object_or_404
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm, AddPersonneForm, DelMachineForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
import logging
from django.http import HttpResponse
from .forms import QuestionForm


def index(request) :
    #on recupere l'ensemble des machines de la database
    machines = Machine.objects.all()
    code = True
    #que l'on passe en parametre de la page html via la syntaxe suivante
    context = {
        'machines' : machines,
    }

    return render(request, 'index.html', context)

def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines': machines}
    return render(request, 'computerApp/machine_list.html',
    context)

@login_required
def personne_list_view(request) : 
    personnes = Personnel.objects.all()
    context={'personnes': personnes}
    return render(request, 'computerApp/personne_list.html',
    context)


def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine': machine}
    return render(request,
    'computerApp/machine_detail.html', context)

@login_required
def personne_detail_view(request, pk):
    personne = get_object_or_404(Personnel, socialsecurity=pk)
    context={'personne': personne}
    return render(request, 'computerApp/personne_detail.html', context)

#formulaire
@login_required
def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            nom= form.cleaned_data.get('nom')
            if nom == 'computerApp/machine_add.html':
                
                return render(request,nom)
            else:
                new_machine = Machine(nom=form.cleaned_data['nom'])
                new_machine.save()
                return redirect('machines')
            
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request, 'computerApp/machine_add.html', context)

@login_required
def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonneForm(request.POST or None)
        if form.is_valid():
            new_personne = Personnel(   
                            nom=form.cleaned_data.get('nom'),
                            socialsecurity=form.cleaned_data.get('socialsecurity'))
            new_personne.save()
        return redirect('personnes')
    else:
        form = AddPersonneForm()
        context = {'form': form}
        return render(request, 'computerApp/personne_add.html', context)

def login_view(request):
    context={}
    return render(request, 'registration/login.html', context)

def logged_out(request):
    logout(request)
    return redirect('index')

@login_required
def del_machine(request):
    if request.method == 'POST':
        form=DelMachineForm(request.POST or None)
        if form.is_valid():
            selected_machine = form.cleaned_data['selected_machine']
            Machine.objects.filter(pk__in=selected_machine).delete()
        return redirect('machines')






@login_required
def questionnaire(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question1 = form.cleaned_data['question1']
            question2 = form.cleaned_data['question2']
            question3 = form.cleaned_data['question3']
            question4 = form.cleaned_data['question4']
            question5 = form.cleaned_data['question5']
            question6 = form.cleaned_data['question6']
            question7 = form.cleaned_data['question7']
            # Traitez les données du formulaire et effectuez les actions nécessaires
            return render(request, 'computerApp/result.html', {'question1': question1, 'question2': question2, 'question3': question3, 'question4': question4, 'question5': question5, 'question6': question6, 'question7': question7})
    else:
        form = QuestionForm()
    
    return render(request, 'computerApp/questionnaire.html', {'form': form, 'show_form': False})



