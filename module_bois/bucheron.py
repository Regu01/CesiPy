# module_bois/bucheron.py
from .employe import Employe

class Bucheron(Employe):
    def __init__(self, nom, salaire, experience):
        super().__init__(nom, salaire)
        self.experience = experience

    def travailler(self):
        print(f"{self.nom} abat des arbres avec {self.experience} d'expérience.")
