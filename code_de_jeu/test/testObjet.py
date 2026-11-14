import unittest
from pgzero.builtins import Actor
from abc import ABC


class objet(ABC, unittest.TestCase):
    """
    Classe dédiée à la base des objets.

    Args:
        ABC (Sans retour): Pour éviter les appels inutiles. 
    """

    vitesse: int
    acteur: Actor
    direction: int 
    "0 = HAUT, 1 = GAUCHE, 2 = BAS et 3 = DROITE"
    vies: int


    def __init__(self, NomImage) -> None:
        self.vitesse = 0
        self.acteur = Actor(NomImage)
        self.direction = 0
        self.vies = 1


    def déplacer(self):
        match self.direction:
            case 0:
                self.acteur.y -= self.vitesse
            case 1:
                self.acteur.x -= self.vitesse
            case 2:
                self.acteur.y += self.vitesse
            case 3:
                self.acteur.x += self.vitesse

    
    def dessiner(self):
        self.acteur.draw()

    def checkCollition(self, acteur) -> bool: 
        return self.acteur.colledirect(acteur)