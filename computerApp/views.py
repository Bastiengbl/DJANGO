from django.shortcuts import render, redirect, get_object_or_404
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm
from django.shortcuts import render


def index(request) :
    #on recupere l'ensemble des machines de la database
    machines = Machine.objects.all()
    
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

def personne_detail_view(request, pk):
    personne = get_object_or_404(Personnel, socialsecurity=pk)
    context={'personne': personne}
    return render(request, 'computerApp/personne_detail.html', context)

#formulaire

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            nom= form.cleaned_data.get('nom')
            if nom == 'computerApp/error.html':
                return render(request,nom)
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request, 'computerApp/machine_add.html', context)

