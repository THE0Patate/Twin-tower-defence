from pgzero.builtins import Actor
from abc import ABC


class objet(ABC):
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
        """
        crée un objet (la base des autre class)
        Args:
            NomImage (image): m'est une image bidon
        """
        self.vitesse = 0
        self.acteur = Actor(NomImage)
        self.direction = 0
        self.vies = 1


    def déplacer(self):
        """
        fonction de deplacement de base
        """
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
        """
        déssine les acteurs a l'écran
        """
        self.acteur.draw()

    def checkCollition(self, acteur) -> bool: 
        return self.acteur.colliderect(acteur)