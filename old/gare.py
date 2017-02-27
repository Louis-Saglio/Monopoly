class Gare:

    def __init__(self, verbose=False):
        self.nom = "Undefined"
        self.prix_achat = "Undefined"
        self.loyer = "Undefined"
        self.est_hypotheque = "Undefined"
        self.est_libre = "Undefined"
        self.valeur_hypotheque = "Undefined"

        if verbose:
            self.set_nom(input('Nom du terrain'))
            self.set_prix_achat(input("Prix du terrain"))

    # Gestion de nom
    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom

    # Gestion de prix_achat
    def get_prix_achat(self):
        return self.prix_achat

    def set_prix_achat(self, new_prix_achat):
        self.prix_achat = new_prix_achat

    # Gestion de loyer
    def get_loyer(self):
        return self.loyer

    def set_loyer(self, new_loyer):
        self.loyer = new_loyer

    # Gestion de est_hypotheque
    def get_est_hypotheque(self):
        return self.est_hypotheque

    def set_est_hypotheque(self, new_est_hypotheque):
        self.est_hypotheque = new_est_hypotheque

    # Gestion de est_libre
    def get_est_libre(self):
        return self.est_libre

    def set_est_libre(self, new_est_libre):
        self.est_libre = new_est_libre

    # Gestion de valeur_hypotheque
    def get_valeur_hypotheque(self):
        return self.valeur_hypotheque

    def set_valeur_hypotheque(self, new_valeur_hypotheque):
        self.valeur_hypotheque = new_valeur_hypotheque
