class Livre:
    def __init__(self, titre):
        self.titre = titre
        self.Auteur = Auteur
    
    def PrintTitle(self):
        print("titre:" + self.titre)

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Auteur(Personne, oeuvre):
    def listerOeuvre(self.titre)
    def ecrireUnLivre()