# module_bois/bucheron.py
from .employe import Employe

class Bucheron(Employe):
    def __init__(self, nom, salaire, experience, barbu):
        super().__init__(nom, salaire)
        self._experience = experience
        self._barbu = barbu

    @property
    def experience(self):
        return self._experience

    def travailler(self):
        print(f"{self.nom} abat des arbres, du haut de ses {self.experience} ans d'expérience.")

    def estBarbu(self):
        if(self._barbu == True):
            print(f"{self.nom} est barbu.")
        else:
            print(f"{self.nom} n'est pas barbu.")
