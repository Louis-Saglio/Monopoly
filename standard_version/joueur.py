class Joueur:

    def __init__(self, nom, capital_depart, position_depart):
        self.nom = nom
        self.capital = capital_depart
        self.position = position_depart
        self.proprietes = []

    def avancer_de(self, nbr_cases, plateau):
        """
        :param nbr_cases: Nombre de case duquel il faut avancer le pion.
        :type nbr_cases: int
        :param plateau: Plateau sur lequel se déplace le pion.
        :type plateau: list
        :return:    None    Modifie directement l'arttribut position de l'objet self.
        """
        for case in range(nbr_cases):
            self.position += 1
            if self.position == len(plateau):
                self.position(0)

    @staticmethod
    def lancer_des(des):
        from random import randint
        rep = 0
        for i in range(des.nombre_de_des):
            rep += randint(1, des.nombre_de_faces)
        return rep

    def payer(self, somme):
        self.capital -= somme

    def recevoir(self, somme):
        self.capital += somme

    def acheter(self, propriete):
        self.payer(propriete.prix_achat)
        self.proprietes.append(propriete)


def creer_joueurs(nbr_joueurs):
    joueurs = []
    for num_joueur in range(nbr_joueurs):
        joueurs.append(Joueur("joueur" + str(num_joueur), 150000, 0))
    return joueurs


if __name__ == "__main__":
    print(creer_joueurs(3))
