from gsm_version import creation_objets

data = creation_objets.run()
plateau = data["terrains"]
joueurs = data["joueurs"]
des = data["des"][0]

jouer = True
while jouer:
    for joueur_courrant in joueurs:
        joueur_courrant.avancer_de(joueur_courrant.lancer_des(des), plateau)
        joueur_courrant.payer(plateau[joueur_courrant.get_position()].get_prix_d_achat_terrain())
        if joueur_courrant.get_argent() <= 0:
            jouer = False
        print("Le joueur", joueur_courrant.get_nom(), "est sur la case",
              plateau[joueur_courrant.get_position()].get_nom())
        print("Il paye donc", plateau[joueur_courrant.get_position()].get_prix_d_achat_terrain())
        print("Il lui reste :", joueur_courrant.get_argent())

# print(plateau, joueurs, des, sep='\n')
