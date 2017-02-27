class Joueur:

    def __init__(self):
        self.nom = "sans-nom"
        self.position = 0
        self.argent = 150000
        self.immobilier = []

    # Gestion du nom
    def get_nom(self):
        return self.nom

    def set_nom(self, newNom):
        self.nom = newNom

    # Gestion de la position
    def get_position(self):
        return self.position

    def set_position(self, newPosition):
        self.position = newPosition

    def avancer_de(self, pas):
        self.set_position(self.get_position() + pas)

    # Gestion de l'argent
    def get_argent(self):
        return self.argent

    def set_argent(self, newArgent):
        self.argent = newArgent

    def depenser(self, somme):
        self.set_argent(self.get_argent() - somme)

    def gagner(self, somme):
        self.set_argent(self.get_argent() - somme)

    # Gestion de l'immobilier
    def get_immobilier(self):
        return self.immobilier

    def set_immobilier(self, newImmobilier):
        self.immobilier = newImmobilier

    def ajouter_propriete(self, newPropriete):
        self.immobilier.append(newPropriete)
