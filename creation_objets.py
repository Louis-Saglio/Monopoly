from getter_setter_maker import create_class_instance


def creer_plateau():

    # Mise en forme du dictionnaire pour la fonction creat_class_instance()
    # Trois attributs : nom, prix_d_achat_terrain, prix_d_achat_maison
    terrains = {
        "nom": [
            "Rue de la paix",
            "Avenue Henri Martin",
            "Place Pigalle",
            "Place de la Bourse"
        ],
        "prix_d_achat_terrain": [
            40000,
            28000,
            20000,
            34000
        ],
        "prix_d_achat_maison": [
            20000,
            15000,
            10000,
            15000
        ]
    }
    return create_class_instance("Terrain", terrains)


def creer_joueurs(nbr_joueurs):

    def demander(nbr):
        rep = []
        for i in range(nbr):
            rep.append(input("Choisissez un nom pour le joueur numéro " + str(i+1)))
        return rep

    joueurs = {
        "nom": demander(nbr_joueurs),
        "argent": [150000] * nbr_joueurs
    }

    return create_class_instance("Joueur", joueurs)


if __name__ == "__main__":
    # Tests
    for terrain in creer_plateau():
        print(terrain.get_nom(), terrain.get_prix_d_achat_terrain(), terrain.get_prix_d_achat_maison())
    for joueur in creer_joueurs(2):
        if joueur.get_nom() == "Louis":
            joueur.set_argent(999999)
        print(joueur.get_nom(), joueur.get_argent())
