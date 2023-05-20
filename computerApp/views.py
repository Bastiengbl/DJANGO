from django.shortcuts import render, redirect, get_object_or_404
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm, AddPersonneForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse


def index(request) :
    #on recupere l'ensemble des machines de la database
    machines = Machine.objects.all()
    
    #que l'on passe en parametre de la page html via la syntaxe suivante
    context = {
        'machines' : machines,
    }

    return render(request, 'index.html', context)
@login_required
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

@login_required
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
            nom=form.cleaned_data.get('nom')
            if nom == 'computerApp/personne_add.html':
                return render(request, nom)
            else:
                new_personne = personne(nom=form.cleaned_data['nom'])
                new_personne.save()
                return redirect('personnes')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request, 'computerApp/personne_add.html', context)


def login_view(request):
    context={}
    code = True
    return render(request, 'registration/login.html', context)



def logged_out(request):
    code = False
    logout(request)
    return redirect('index')


