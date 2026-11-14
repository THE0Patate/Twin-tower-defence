from LaProjectile import LaProjectile
from pgzero.builtins import Actor

class Projectile_H(LaProjectile):
    """
    Classe des projectiles de l'hélicoptere.

    Args:
        LaProjectile (Classe parente): La classe des projectiles.
    """
    
    vitesse: int
    direction: int
    vies: int
    


    def __init__(self, y) -> None:
        """
        Création d'un missile d'hélicoptaire

        Args:
            y (int): y est la position de l'hélicoptaire en y
        """
        super().__init__("missile_final.png")
        self.acteur.x = 1100
        self.acteur.y = y
        self.direction = 1


    def déplacer(self):
        """
        Déplace les projectiles de l'hélicoptaire
        """
        super().déplacer()

    