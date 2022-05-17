from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import EquipeForm, JoueurForm


# Create your views here

def ajout(request):
    if request.method == "POST":
        form = EquipeForm(request)
        return render(request, "appli_bball/ajout.html", {"form": form})
    else:
        form = EquipeForm()
        return render(request, "appli_bball/ajout.html", {"form": form})


def recrute(request):
    if request.method == "POST":
        form = JoueurForm(request)
        return render(request, "appli_bball/recrute.html", {"form": form})
    else:
        form = JoueurForm()
        return render(request, "appli_bball/recrute.html", {"form": form})


def saisie(request):
    return render(request, "appli_bball/saisie.html")


def traitement(request):
    eform = EquipeForm(request.POST)
    if eform.is_valid():
        equipe = eform.save()
        return HttpResponseRedirect("/appli_bball")
    else:
        return render(request, "appli_bball/ajout.html", {"form": eform})


def traitementj(request):
    jform = JoueurForm(request.POST)
    if jform.is_valid():
        joueur = jform.save()
        return HttpResponseRedirect("/appli_bball")
    else:
        return render(request, "appli_bball/recrute.html", {"form": jform})


def index(request):
    liste = list(models.Equipe.objects.all())
    listej = list(models.Joueur.objects.all())
    return render(request, "appli_bball/index.html", {"liste": liste, "listej": listej})


def affiche(request, id):
    equipe = models.Equipe.objects.get(pk=id)
    return render(request, "appli_bball/affiche.html", {"equipe": equipe})


def affichej(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    return render(request, "appli_bball/affichej.html", {"joueur": joueur})


def update(request, id):
    equipe = models.Equipe.objects.get(pk=id)
    form = EquipeForm(equipe.dico())
    return render(request, "appli_bball/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    eform = EquipeForm(request.POST)
    if eform.is_valid():
        equipe = eform.save(commit=False)
        equipe.id = id
        equipe.save()
        return HttpResponseRedirect("/appli_bball")
    else:
        return render(request, "appli_bball/ajout.html", {"form": eform, "id": id})


def delete(request, id):
    equipe = models.Equipe.objects.get(pk=id)
    equipe.delete()
    return HttpResponseRedirect("/appli_bball")


def deletej(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    joueur.delete()
    return HttpResponseRedirect("/appli_bball")


def updatej(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    form = JoueurForm(joueur.dico())
    return render(request, "appli_bball/ajout.html", {"form": form, "id": id})


def updatetraitementj(request, id):
    jform = JoueurForm(request.POST)
    if jform.is_valid():
        joueur = jform.save(commit=False)
        joueur.id = id
        joueur.save()
        return HttpResponseRedirect("/appli_bball")
    else:
        return render(request, "appli_bball/ajout.html", {"form": jform, "id": id})
