class Des:

    def __init__(self, attributs):
        self.attr = attributs
        self.set_nombre_de_faces(attributs["nombre_de_faces"])
        self.set_nombre_de_des(attributs["nombre_de_des"])
        # Attention ! Toujours laisser la ligne suivante a la fin de la methode init
        # Fin de la methode init

    # Gestion de nombre_de_faces
    def get_nombre_de_faces(self):
        return self.nombre_de_faces

    def set_nombre_de_faces(self, new_nombre_de_faces):
        self.nombre_de_faces = new_nombre_de_faces

    # Gestion de nombre_de_des
    def get_nombre_de_des(self):
        return self.nombre_de_des

    def set_nombre_de_des(self, new_nombre_de_des):
        self.nombre_de_des = new_nombre_de_des

