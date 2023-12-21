# module_bois/ressources_forestieres.py

class RessourcesForestieres:
    def __init__(self, quantite):
        self._quantite = quantite

    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, nouvelle_quantite):
        if nouvelle_quantite >= 0:
            self._quantite = nouvelle_quantite
        else:
            print("Erreur : La quantité ne peut pas être négative.")

    def recolter(self):
        print(f"Récolte de ressources forestières: {self.quantite} tonnes.")
