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

    def recolter(self, quantite_recoltee):
        if quantite_recoltee > 0 and self.quantite >= quantite_recoltee:
            print(f"Récolte de ressources forestières: {quantite_recoltee} tonnes.")
            self.quantite += quantite_recoltee
        else:
            print("Erreur : La quantité à récolter est invalide.")
