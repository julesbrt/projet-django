from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),

    # path('saisie/', views.saisie),

    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>/", views.updatetraitement),
    path("updatetraitement//", views.traitement),
    path("delete/<int:id>/", views.delete),



    path('recrute/', views.recrute),
    path('traitementj/', views.traitementj),
    path("affichej/<int:id>/", views.affichej),
    path("updatej/<int:id>/", views.updatej),
    path("updatetraitementj/<int:id>/", views.updatetraitementj),
    path("updatetraitementj//", views.traitementj),
    path("deletej/<int:id>/", views.deletej),


]