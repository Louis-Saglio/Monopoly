class Joueur:

    def __init__(self, attributs):
        self.attr = attributs
        self.set_nom(attributs["nom"])
        self.set_argent(attributs["argent"])
        self.set_position(attributs["position"])
        # Attention ! Toujours laisser la ligne suivante a la fin de la methode init
        # Fin de la methode init

    # Gestion de nom
    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom

    # Gestion de argent
    def get_argent(self):
        return self.argent

    def set_argent(self, new_argent):
        self.argent = new_argent

    def payer(self, somme):
        self.set_argent(self.get_argent() - somme)

    # Gestion de position
    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def avancer_de(self, nbr_cases, plateau):
        """
        :param nbr_cases:   int     Nombre de case duquel il faut avancer le pion.
        :param plateau:     list    Plateau sur lequel se déplace le pion.
        :return:    None    Modifie directement l'arttribut position de l'objet self.
        """
        for case in range(nbr_cases):
            self.set_position(self.get_position()+1)
            if self.get_position() == len(plateau):
                self.set_position(0)

    @staticmethod
    def lancer_des(des):
        from random import randint
        rep = 0
        for i in range(des.nombre_de_des):
            rep += randint(1, des.nombre_de_faces)
        return rep


if __name__ == "__main__":
    from random import randint
    j = Joueur({"nom": "test", "argent": 150000, "position": 0})
    from gsm_version.getter_setter_maker import require
    print("Lancer des des :", j.lancer_des(require("Des")({"nombre_de_faces": 6, "nombre_de_des": 2})))
    j.avancer_de(randint(2, 12), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("Position :", j.position)
