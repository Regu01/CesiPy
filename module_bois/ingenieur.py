# module_bois/ingenieur.py
from .employe import Employe

class Ingenieur(Employe):
    def __init__(self, nom, salaire, competence):
        super().__init__(nom, salaire)
        self.competence = competence

    def travailler(self):
        print(f"{self.nom} travaille sur des projets d'ingénierie.")
