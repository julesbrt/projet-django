from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    #path('saisie/', views.saisie),
    path('traitement/', views.traitement),
    path("", views.index),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),

    path("updatetraitement/<int:id>/", views.updatetraitement),

    path("updatetraitement//", views.traitement),

    path("delete/<int:id>/", views.delete),
]