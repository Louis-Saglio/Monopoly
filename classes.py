class Terrain:

    def __init__(self, attributs):
        self.attr = attributs
        self.set_prix_d_achat_terrain(attributs["prix_d_achat_terrain"])
        self.set_prix_d_achat_maison(attributs["prix_d_achat_maison"])
        self.set_nom(attributs["nom"])

    # Gestion de prix_d_achat_terrain
    def get_prix_d_achat_terrain(self):
        return self.prix_d_achat_terrain

    def set_prix_d_achat_terrain(self, new_prix_d_achat_terrain):
        self.prix_d_achat_terrain = new_prix_d_achat_terrain

    # Gestion de prix_d_achat_maison
    def get_prix_d_achat_maison(self):
        return self.prix_d_achat_maison

    def set_prix_d_achat_maison(self, new_prix_d_achat_maison):
        self.prix_d_achat_maison = new_prix_d_achat_maison

    # Gestion de nom
    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom


class Joueur:

    def __init__(self, attributs):
        self.attr = attributs
        self.set_argent(attributs["argent"])
        self.set_nom(attributs["nom"])

    # Gestion de argent
    def get_argent(self):
        return self.argent

    def set_argent(self, new_argent):
        self.argent = new_argent

    # Gestion de nom
    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom


