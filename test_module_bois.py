# tests/test_module_bois.py
import unittest
from module_bois.ingenieur import Ingenieur
from module_bois.bucheron import Bucheron
from module_bois.entreprise_bois import EntrepriseBois
from module_bois.ressources_forestieres import RessourcesForestieres
from module_bois.produits_bois import ProduitBois

class TestModuleBois(unittest.TestCase):
    def test_embauche_licenciement(self):
        ingenieur1 = Ingenieur("Alice", 60000, "Conception")
        bucheron1 = Bucheron("Bob", 50000, 3, False)
        entreprise_bois = EntrepriseBois("BoisPro", [ingenieur1, bucheron1], RessourcesForestieres(200))

        nouveau_bucheron = Bucheron("Charlie", 55000, 5, True)
        entreprise_bois.embaucher(nouveau_bucheron)

        self.assertEqual(len(entreprise_bois.employes), 3)

        entreprise_bois.licencier(ingenieur1)
        self.assertEqual(len(entreprise_bois.employes), 2)

    def test_travail_ressources(self):
        bucheron = Bucheron("Bob", 50000, 3, False)
        ressources = RessourcesForestieres(100)
        entreprise_bois = EntrepriseBois("BoisPro", [bucheron], ressources)

        entreprise_bois.effectuer_travail()
        bucheron.travailler()
        
        self.assertEqual(ressources.quantite, 100)
        
        entreprise_bois.recolter_ressources(100)

        self.assertEqual(ressources.quantite, 200)

if __name__ == '__main__':
    unittest.main()
