# ecole/personne.py

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Age: {self.age}")
