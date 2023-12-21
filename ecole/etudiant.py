# ecole/etudiant.py
from .personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Matricule: {self.matricule}")

    def adapter(self):
        print(f"L'étudiant {self.nom} s'adapte bien.")
