from Objet import objet
from pgzero.builtins import Actor
import unittest


class LaProjectile(objet, unittest.TestCase):
    """
    Classe parent des projectile

    Args:
        object (Classe parente): Classe qui représente un objet
    """
    
    vitesse: int
    direction: int
    vies: int

    def __init__(self) -> None:
        super().__init__("MissileFinal.png")
        self.direction = 0
        self.vitesse = 1

    def déplacer(self):
        super().déplacer()
        self.vitesse *= 2