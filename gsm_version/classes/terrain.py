class Terrain:

    def __init__(self, attributs):
        self.attr = attributs
        self.set_nom(attributs["nom"])
        self.set_prix_d_achat_terrain(attributs["prix_d_achat_terrain"])
        self.set_prix_d_achat_maison(attributs["prix_d_achat_maison"])
        # Attention ! Toujours laisser la ligne suivante a la fin de la methode init
        # Fin de la methode init

    # Gestion de nom
    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom

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

