from pgzero.builtins import Actor
from Avion import Avion
import random

class Mechant(Avion):
    """
    La classe des bad boys terroristes. 

    Args:
        Avion (Classe parente): Classe qui représente un objet volant.
    """
    
    vitesse: int
    direction: int
    vies: int
    
    def __init__(self) -> None:
        """
        Creation d'une avion méchante
        """
        super().__init__("avion_t.png")
        