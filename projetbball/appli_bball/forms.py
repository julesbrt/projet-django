from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class EquipeForm(ModelForm):
    class Meta:
        model = models.Equipe

        fields = ('nom', 'ville', 'datecrea', 'proprio', 'sponsor', 'coach', 'nbrtrophee')
        labels = {
            'nom': _('Nom équipe'),
            'ville': _('Ville'),
            'datecrea': _('Date de creation'),
            'proprio': _('Propriétaire'),
            'sponsor': _('Sponsor'),
            'coach': _('Coach'),
            'nbrtrophee': _('Nombre de trophée(s)'),

        }


class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur

        fields = ('nomj', 'prenom', 'taille', 'poids', 'poste', 'numero', 'nbrtropheej', 'equipe')
        labels = {
            'nomj': _('Nom joueur '),
            'prenom': _('Prénom '),
            'taille': _('Taille '),
            'poids': _('Poids '),
            'poste': _('Poste '),
            'numero': _('Numéro '),
            'nbrtropheej': _('Nombre de trophée(s) '),
            'equipe': _('Equipe '),
        }
