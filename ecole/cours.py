# ecole/cours.py
class Cours:
    def __init__(self, nom_cours, professeur, etudiants):
        self.nom_cours = nom_cours
        self.professeur = professeur
        self.etudiants = etudiants

    def afficher_infos(self):
        print(f"Nom du cours: {self.nom_cours}")
        print("Informations sur le professeur:")
        self.professeur.afficher_infos()
        print("\nListe des étudiants:")
        for etudiant in self.etudiants:
            etudiant.afficher_infos()
