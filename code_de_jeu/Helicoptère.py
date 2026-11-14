from Objet import objet
from pgzero.builtins import Actor

class helicoptere(objet):
    """
    Classe de l'hélico qui va protêger les twins tower.

    Args:
        objet (Classe parente): Classe qui représente un objet
    """

    vitesse: int
    direction: int

    def __init__(self) -> None:
        """
        Création de l'hélicoptère
        """
        super().__init__("helicoptere_final.png")
        self.acteur.x = 1000
        self.acteur.y = 300
        self.vitesse = 5

    def choisirDirection(self, clavier):
        """
        choisi la direction selon le imput du clavier

        Args:
            clavier (_type_): recoi la touche apuiyer par le clavier
        """
        if clavier.up:
            self.direction = 0
        elif clavier.down:
            self.direction = 2
        else:
            return
        

    def déplacer(self):
        """
        Déplace l'hélicoptaire
        """
        match self.direction:
            case 0:
                if self.acteur.y > 0:
                    super().déplacer()
            case 2:
                if self.acteur.y < 600:
                    super().déplacer()