from pgzero.builtins import Actor
from Objet import objet
import random

class Tank(objet):
    """
    Class qui crée et représente le Tank.

    Args:
        object (Classe parente): Classe qui représente un objet
    """

    vitesse: int
    direction: int
    vies: int

    def __init__(self) -> None:
        """
        création du Tank
        """
        super().__init__("tank.png")
        self.acteur.y = 550
        self.acteur.x = 800
        self.direction = 1
        self.vitesse = 10

    def choisirDirection(self):
        """
        choisi aléatoirement la direction que le Tank va se diriger
        """
        if random.randint(0,50) == 42:
            self.direction = random.choice([1,3])
        if self.acteur.x <= 10:
            if random.randint(0,8) == 5:
                self.direction = 3
        if self.acteur.x >= 1000:
            if random.randint(0,8) == 5:
                self.direction = 1

    def déplacer(self):
        """
        déplace le Tank
        """
        match self.direction:
            case 1:
                if self.acteur.x > 0:
                    super().déplacer()
            case 3:
                if self.acteur.x < 1000:
                    super().déplacer()