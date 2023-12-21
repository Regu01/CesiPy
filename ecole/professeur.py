# ecole/professeur.py
from .personne import Personne

class Professeur(Personne):
    def __init__(self, nom, prenom, age, specialite):
        super().__init__(nom, prenom, age)
        self.specialite = specialite

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Spécialité: {self.specialite}")

    def adapter(self):
        print(f"Le professeur {self.nom} s'adapte bien.")
