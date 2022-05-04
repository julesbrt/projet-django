from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EquipeForm(ModelForm):
    class Meta:
        model = models.equipe

        fields = ('nom', 'ville','datecrea', 'proprio', 'sponsor', 'coach','nbrtrophee')
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
        model = models.joueur

        fields = ('nomj', 'prenom','taille', 'poids', 'poste', 'numero', 'nbrtropheej')
        labels = {
            'nomj': _('Nom joueur'),
            'prenom': _('prénom'),
            'taille': _('taille'),
            'poids': _('poids'),
            'poste': _('poste'),
            'numero': _('numéro'),
            'nbrtropheej': _('Nombre de trophée(s)'),
        }