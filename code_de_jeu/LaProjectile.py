from Objet import objet
from pgzero.builtins import Actor


class LaProjectile(objet):
    """
    Classe parent des projectile

    Args:
        object (Classe parente): Classe qui représente un objet
    """
    
    vitesse: int
    direction: int
    vies: int

    def __init__(self, nom_image) -> None:
        """
        Création de la base des projectile
        Args:
            nom_image (image): attribu une image bidon
        """
        super().__init__(nom_image)
        self.direction = 0
        self.vitesse = 1

    def déplacer(self):
        """
        Déplace les projectile
        """
        super().déplacer()
        self.vitesse += 1