def create_class(verbose=False, nom_classe=None, input_attributs=None, tab='    '):
    if verbose:
        nom_classe = input("Entrez le nom de la classe: ")
        input_attributs = input("Entrez le nom des attributs séparés par des virgules:  ")
        input_attributs += ','
        attributs = []
        attr = ''
        for lettre in input_attributs:
            if lettre != ',':
                attr += lettre
            else:
                attributs.append(attr)
                attr = ''

    with open("classes.py", 'a') as dest:
        print("class ", nom_classe, ':\n', sep='', file=dest)
        print(tab, "def __init__(self, attributs):", sep='', file=dest)
        print(tab, tab, "self.attr = attributs", sep='', file=dest)
        for attribut in attributs:
            print(tab, tab, "self.set_", attribut, "(attributs[\"", attribut, "\"])", sep='', file=dest)
        print("\n", end='', file=dest)
        for attribut in attributs:
            print(tab, "# Gestion de ", attribut, sep='', file=dest)
            print(tab, "def get_", attribut, "(self):\n", tab, tab, "return self.", attribut, sep='', end='\n\n', file=dest)
            print(tab, "def set_", attribut, "(self, new_", attribut, "):\n", tab, tab, "self.", attribut, " = new_", attribut, sep='', end='\n\n', file=dest)
        print("\n\n\n", sep='', end="\n", file=dest)


def create_object(classe, attributs):
    from copy import deepcopy
    objets = []
    noms_attr = []
    dico = {}
    for key in attributs:
        noms_attr.append(key)
        dico[key] = []
    for i in range(len(attributs[noms_attr[0]])):
        for n in noms_attr:
            dico[n] = attributs[n][i]
        objets.append(classe(dico))
        objets = deepcopy(objets)
    return objets


def create_class_instance(nom_classe, attributs):
    classe = interprete(nom_classe)
    try:
        from classes import classe
    except:
        create_class(nom_classe, attributs)
        from classes import classe
    objets = create_object(classe, attributs)


if __name__ == "__main__":
    create_class(nom_classe="Pion", input_attributs="nom,position")
    from classes import Pion
    objets = create_object(Pion, {"nom": ["pion1", "pion2"], "position": [1, 2]})
    print(objets[1].get_nom(), objets[0].get_position())
    # from os import remove
    # remove("classes/pion.py")