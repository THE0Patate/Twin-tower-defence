from LaProjectile import LaProjectile
from pgzero.builtins import Actor

class Projectile_A(LaProjectile):
    """
    Classe des projectiles du tank.

    Args:
        LaProjectile (Classe parente): La classe des projectiles.
    """
    
    vitesse: int
    direction: int
    vies: int


    def __init__(self, x) -> None:
        """
        Création du projectile du Tank

        Args:
            x (int): rapporte la position du Tank en x
        """
        super().__init__("grosmissilefinal.png")
        self.acteur.x = x
        self.acteur.y = 550
        self.direction = 0
        

    def déplacer(self):
        """
        Déplace les projectile du Tank
        """
        super().déplacer()