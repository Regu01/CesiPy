# main.py
from module_bois.ingenieur import Ingenieur
from module_bois.bucheron import Bucheron
from module_bois.entreprise_bois import EntrepriseBois
from module_bois.ressources_forestieres import RessourcesForestieres
from module_bois.produits_bois import ProduitBois

def main():
    # Création des employés
    ingenieur1 = Ingenieur("Alice", 60000, "Conception")
    bucheron1 = Bucheron("Bob", 50000, 3)

    # Création de l'entreprise avec un bucheron initial
    entreprise_bois = EntrepriseBois("BoisPro", [bucheron1], RessourcesForestieres(100))

    # Embauche d'un nouvel employé
    nouveau_bucheron = Bucheron("Charlie", 55000, 5)
    entreprise_bois.embaucher(nouveau_bucheron)

    # Effectuer le travail dans l'entreprise
    entreprise_bois.effectuer_travail()

    # Recolter des ressources forestières
    entreprise_bois.recolter_ressources()

    # Production et vente de produits en bois
    produit_bois = ProduitBois("Planche de chêne", 20)
    entreprise_bois.produire_bois(produit_bois)
    entreprise_bois.vendre_produits()

    # Embauche d'un ingénieur
    entreprise_bois.embaucher(ingenieur1)

    # Licenciement d'un employé
    entreprise_bois.licencier(ingenieur1)

if __name__ == "__main__":
    main()
