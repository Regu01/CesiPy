# module_bois/employe.py

class Employe:
    def __init__(self, nom, salaire):
        self._nom = nom
        self._salaire = salaire

    @property
    def nom(self):
        return self._nom

    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, nouveau_salaire):
        if nouveau_salaire >= 0:
            self._salaire = nouveau_salaire
        else:
            print("Erreur : Le salaire ne peut pas être négatif.")

    def travailler(self):
        pass
