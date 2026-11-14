from Avion import Avion
from pgzero.builtins import Actor
import random

class Gentil(Avion):
    """
    Classe de l'avion pas terroriste qui va apporter des munitions pour le tank.

    Args:
        Avion (Classe parente): Classe qui représente un objet volant.
    """
    
    vitesse: int
    direction: int
    vies: int

    def __init__(self) -> None:
        """
        Création de l'avion pas terroriste.
        """
        super().__init__("avion_g.png")
        
    