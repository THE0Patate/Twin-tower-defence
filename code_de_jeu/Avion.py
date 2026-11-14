from pgzero.builtins import Actor
from Objet import objet
import random

class Avion(objet):
    """
    La classe des objets volant. 

    Args:
        objet (Classe parente): Classe qui représente un objet
    """
    
    vitesse: int
    direction: int
    vies: int
    
    def __init__(self, nom_image) -> None:
        """
        Création de l'avion.

        Args:
            nom_image (str): l'image de l'avion.
        """
        super().__init__(nom_image)
        self.direction = random.choice([0,2])
        self.vitesse = 3
        self.acteur.x = -50
        self.acteur.y = random.randint(0, 600)

    def choisirDirection(self):
        """
        Fonction qui choisi la direction de l'avion.
        """
        if random.randint(0,30) == 22:
            self.direction = random.choice([0,2])
        if self.acteur.y <= 0:
            if random.randint(0,8) == 5:
                self.direction = 2
        if self.acteur.y >= 600:
            if random.randint(0,8) == 5:
                self.direction = 0

    def déplacer(self):
        """
        Fonction qui déplace l'avion.
        """
        self.acteur.x += self.vitesse
        match self.direction:
            case 0:
                if self.acteur.y > 0:
                    super().déplacer()
            case 2:
                if self.acteur.y < 600:
                    super().déplacer()