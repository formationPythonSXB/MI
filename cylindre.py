from cercle import Cercle


class Cylindre(Cercle):

    def __init__(self, rayon, hauteur, centre):
        self.hauteur = hauteur
        super().__init__(rayon, centre)

    def intersect(self, c2):
        if super().intersect(c2) and c2.centre[2] - self.centre[2] < (c2.hauteur + self.hauteur) / 2:
            return True
        else:
            return False
