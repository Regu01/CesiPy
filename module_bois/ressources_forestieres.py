# module_bois/ressources_forestieres.py

class RessourcesForestieres:
    def __init__(self, quantite):
        self.quantite = quantite

    def recolter(self):
        print(f"Récolte de ressources forestières: {self.quantite} tonnes.")
