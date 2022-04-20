class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


    def SePresenter(self):
        print("prenom :" + self.prenom)
        print("nom :" + self.nom)

p1 = Personne("Jul","Sakakini")
p2 = Personne("Joris","Verguldezoone")
p3 = Personne("Fabien","Palace")
p4 = Personne("Dorian","Ponzio")

p2.SePresenter()


