# module_bois/entreprise_bois.py
from .ingenieur import Ingenieur
from .bucheron import Bucheron
from .ressources_forestieres import RessourcesForestieres
from .produits_bois import ProduitBois

class EntrepriseBois:
    def __init__(self, nom, employes, ressources_forestieres):
        self.nom = nom
        self.employes = employes
        self.ressources_forestieres = ressources_forestieres
        self.produits = []

    def embaucher(self, employe):
        self.employes.append(employe)
        print(f"{employe.nom} a été embauché chez {self.nom}.")

    def licencier(self, employe):
        self.employes.remove(employe)
        print(f"{employe.nom} a été licencié de {self.nom}.")

    def effectuer_travail(self):
        for employe in self.employes:
            employe.travailler()

    def recolter_ressources(self):
        self.ressources_forestieres.recolter()

    def produire_bois(self, produit):
        self.produits.append(produit)
        print(f"{produit.nom} a été produit.")

    def vendre_produits(self):
        for produit in self.produits:
            produit.vendre()
