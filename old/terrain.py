class Terrain:

    def __init__(self, verbose=False, auto=False, nom='', prix_achat='', loyer='', valeur_hypotheque=''):
        self.nom = "Default"
        self.prix_achat = "Undefined"
        self.loyer = {"Terrain nu": 0, "1 maison": 0, "2 maisons": 0, "3 maisons": 0, "4 maisons": 0, "Hotel": 0}
        self.valeur_hypotheque = 0
        self.est_hypotheque = False
        self.est_libre = True
        self.groupe = "None"

        if verbose:
            self.set_nom(input("Nom du terrain"))
            self.set_prix_achat(input("Prix du terrain"))
            for type_loyer in self.loyer:
                self.set_loyer_detail(type_loyer, input("Montant du loyer"))
            self.set_valeur_hypotheque(input("Valeur de l'hypotheque"))
            self.set_groupe(input("Groupe"))

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

    def set_loyer_detail(self, key, new_loyer):
        self.loyer[key] = new_loyer

    # Gestion de valeur_hypotheque
    def get_valeur_hypotheque(self):
        return self.valeur_hypotheque

    def set_valeur_hypotheque(self, new_valeur_hypotheque):
        self.valeur_hypotheque = new_valeur_hypotheque

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

    # Gestion de groupe
    def get_groupe(self):
        return self.groupe

    def set_groupe(self, new_groupe):
        self.groupe = new_groupe
