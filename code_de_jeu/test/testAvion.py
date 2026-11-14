from pgzero.builtins import Actor
from Objet import objet
import unittest
import random

class Avion(objet, unittest.TestCase):
    """
    La classe des objets volant. 

    Args:
        objet (Classe parente): Classe qui représente un objet
    """
    
    vitesse: int
    direction: int
    vies: int
    
    def __init__(self, nom_image) -> None:
        super().__init__(nom_image)
        self.direction = random.choice([0,2])
        self.vitesse = 5
        self.acteur.x = -50
        self.acteur.y = random.randint(0, 600)

    def choisirDirection(self):
        if random.randint(0,50) == 42:
            self.direction = random.choice([0,2])

    def déplacer(self):
        self.acteur.x += self.vitesse
        match self.direction:
            case 0:
                if self.acteur.y > 0:
                    super().déplacer()
            case 2:
                if self.acteur.y < 600:
                    super().déplacer()