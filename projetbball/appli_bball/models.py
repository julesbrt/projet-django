from django.db import models

# Create your models here.

class equipe(models.Model):
    nom = models.CharField(max_length=30)
    ville = models.CharField(max_length=30)
    datecrea = models.DateField()
    proprio = models.CharField(max_length=30)
    sponsor = models.CharField(max_length=30)
    coach = models.CharField(max_length=30)
    nbrtrophee = models.IntegerField(blank=True)

    def __str__(self):
        return f"Les {self.nom} de {self.ville} sont une franchise de basket-ball en NBA crée le {self.datecrea}." \
               f"Elle appartient à {self.proprio}, son sponsor principale est {self.sponsor}. Le coach principale est" \
               f"{self.coach} et a gagnée un total de {self.nbrtrophee} trophées."


    def dico(self):
        return {"nom":self.nom,"ville":self.ville,"datecrea":self.datecrea,"proprio":self.proprio,"sponsor":self.sponsor,"coach":self.coach,"nbrtrophee":self.nbrtrophee}


class joueur(models.Model):
    nomj = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    taille = models.CharField(max_length=30)
    poids = models.CharField(max_length=30)
    poste = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)
    nbrtropheej = models.IntegerField(blank=True)
    #nbrtropheej = models.MultipleChoice[('PG','point guard'), ('SG','shooting guard'), ('SF','small forward'), ('PF','power forward'), ('C','center')]

    def __str__(self):
        return f"{self.nomj} {self.prenom}  est un joueur de basketball évoluant au poste {self.poste}, il mesure {self.taille}m "\
               f"et pèse {self.poids} kgs. Il porte le numéro {self.numero} et a déjà gagné {self.nbrtropheej} titre(s) de champion NBA."

    def dico(self):
        return {"nomj":self.nomj,"prenom":self.prenom,"taille":self.taille,"poids":self.poids,"poste":self.poste,"numero":self.numero,"nbrtropheej":self.nbrtropheej}