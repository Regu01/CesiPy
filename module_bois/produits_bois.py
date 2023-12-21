# module_bois/produits_bois.py

class ProduitBois:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def vendre(self):
        print(f"Vente du produit en bois '{self.nom}' au prix de {self.prix} euros.")
