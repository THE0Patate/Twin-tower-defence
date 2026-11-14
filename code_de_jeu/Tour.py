from Objet import objet
from pgzero.builtins import Actor

class tour(objet):
    """
    Classe qui repésente les tours.

    Args:
        objet (Classe parente): Classe qui représente un objet
    """

    vies: int


    def __init__(self) -> None:
        """
        Création de la tour.
        """
        super().__init__("twin_tower.png")
        self.acteur.x = 1100
        self.acteur.y = 300
        self.vies = 2

    def collisionMechant(self):
        """
        Vérifie le nombre de point de vie de la tour pour ajusté l'image de la tour selon ses point de vie
        """
        self.vies -= 1
        if self.vies == 1:
            self.acteur.image = "touw_brisé_final.png"
        if self.vies == 0:
            self.acteur.image = "explosion.jpeg"

    def tourTombé(self) -> bool:
        if self.acteur.image == "explosion.jpeg":
            return True
        return False
