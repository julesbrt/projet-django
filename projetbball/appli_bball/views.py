from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import EquipeForm

# Create your views here

def ajout(request):
    if request.method == "POST":
        form = EquipeForm(request)
        return render(request, "appli_bball/ajout.html", {"form": form})
    else :
        form = EquipeForm()
        return render(request, "appli_bball/ajout.html", {"form": form})

def recrute(request):
    if request.method == "POST":
        form = EquipeForm(request)
        return render(request, "appli_bball/recrute.html", {"form": form})
    else :
        form = EquipeForm()
        return render(request, "appli_bball/recrute.html", {"form": form})

def saisie(request):
    return render(request, "appli_bball/saisie.html")

def traitement(request):
    eform = EquipeForm(request.POST)
    if eform.is_valid():
        equipe = eform.save()
        return HttpResponseRedirect("/appli_bball")
    else :
        return render(request, "appli_bball/ajout.html", {"form": eform})

def index(request):
    liste = list(models.equipe.objects.all())
    return render(request,"appli_bball/index.html", {"liste": liste})

def affiche(request, id):
    equipe = models.equipe.objects.get( pk = id)
    return render(request, "appli_bball/affiche.html", {"equipe" : equipe})

def update(request, id):
    equipe = models.equipe.objects.get(pk = id)
    form = EquipeForm(equipe.dico())
    return render(request, "appli_bball/ajout.html",{"form":form, "id": id})

def updatetraitement(request, id):

    eform = EquipeForm(request.POST)
    if eform.is_valid():
        equipe = eform.save(commit = False)
        equipe.id = id
        equipe.save()
        return HttpResponseRedirect("/appli_bball")
    else:
        return render(request, "appli_bball/ajout.html", {"form": eform, "id" : id})

def delete(request, id):
    equipe = models.equipe.objects.get(pk=id)
    equipe.delete()
    return HttpResponseRedirect("/appli_bball")
