import pgzrun
from Tank import Tank
from Projectile_A import Projectile_A
from Projectile_H import Projectile_H
from Gentil import Gentil
from Méchant import Mechant
from Tour import tour
from Helicoptère import helicoptere
import random
from code_de_l_application_web.Contrôle import Controle


HEIGHT = 600
WIDTH = 1200


class Jeu:
    """
    Classe du jeu. Cette classe a pour objectif de s'occuper,
    tant du début jusqu'à la fin, du maintient du jeu.
    """

    score: int
    compteur_missile_réserve: int
    game_over_HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE: bool
    projectiles_A: list[Projectile_A]
    projectiles_H: list[Projectile_H]
    tank: Tank
    mechant: list[Mechant]
    gentil: Gentil
    Tour: tour
    Helicoptere: helicoptere
    compteur_missile_temps: int
    compteur_missile_temps_2: int
    compteur_fin: int
    son_avion: str

    
    def __init__(self) -> None:
        """
        Création des variables de la classe jeu.
        """
        self.compteur_missile_réserve = 0
        self.game_over_HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE = False
        self.projectiles_A = []
        self.projectiles_H = []
        self.tank = Tank()
        self.mechant = []
        self.gentil = Gentil()
        self.Tour = tour()
        self.Helicoptere = helicoptere()
        self.score = 0
        self.compteur_missile_temps = 0
        self.compteur_missile_temps_2 = 0
        self.compteur_fin = 0
        self.son_avion = ""
        self.Jouer_son_jeu(sounds)

    def miseAJour(self, clavier):
        """
        Fonction qui se met à jour à tout les FPS (Frame per second).

        Args:
            clavier (_type_): L'état du clavier.
        """
        
        # Vérifit que le jeu est fini.
        if self.game_over_HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE:
            return
        
        # Déplacement du Tank.
        self.tank.choisirDirection()
        self.tank.déplacer()

        # Zone Missiles.
        if clavier.right and self.compteur_missile_réserve > 0 and self.compteur_missile_temps_2 >= 25:
            self.projectiles_A.append(Projectile_A(self.tank.acteur.x))
            self.compteur_missile_réserve -= 1

        for element in self.projectiles_A:
            element.déplacer()
        
        if clavier.left and len(self.projectiles_H) <= 6 and self.compteur_missile_temps >= 25:
            self.projectiles_H.append(Projectile_H(self.Helicoptere.acteur.y))
            self.compteur_missile_temps = 0

        self.compteur_missile_temps += 1
        self.compteur_missile_temps_2 += 1

        for element in self.projectiles_H:
            element.déplacer()
        
        # Zone Avion terroriste.
        if len(self.mechant) < 5 and random.randint(0,50) == 22:
            self.mechant.append(Mechant())

        for mesquin in self.mechant:
            mesquin.choisirDirection()
            mesquin.déplacer()
            if mesquin.checkCollition(self.Tour.acteur):
                sounds.tourexplosion.play()
                self.mechant.remove(mesquin)
                self.Tour.collisionMechant()
                self.score -= 6900
                if self.Tour.tourTombé():
                    self.game_over_HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE = True

            if mesquin != None:
                for element in self.projectiles_A:
                    if mesquin.checkCollition(element.acteur) and len(self.projectiles_A) != 0:
                        sounds.explosion.play()
                        self.projectiles_A.remove(element)
                        self.mechant.remove(mesquin)
                        self.score += 100

            if mesquin != None:
                for element in self.projectiles_H:
                    if mesquin.checkCollition(element.acteur) and len(self.projectiles_H) != 0:
                        sounds.explosion.play()
                        self.projectiles_H.remove(element)
                        self.mechant.remove(mesquin)
                        self.score += 100


        # Zone Avion pas terroriste.
        self.gentil.déplacer()
        self.gentil.choisirDirection()
        if self.gentil.checkCollition(self.Tour.acteur):
            self.gentil = None
            self.score += 1000
            self.compteur_missile_réserve += 1

        for element in self.projectiles_A:
            if self.gentil != None:
                if self.gentil.checkCollition(element.acteur) and len(self.projectiles_A) != 0:
                    sounds.explosion.play()
                    self.projectiles_A.remove(element)
                    self.gentil = None
                    self.score -= 100
                if element.acteur.y < 0:
                    self.projectiles_A.remove(element)

        for element in self.projectiles_H:
            if self.gentil != None:
                if self.gentil.checkCollition(element.acteur) and len(self.projectiles_H) != 0:
                    sounds.explosion.play()
                    self.projectiles_H.remove(element)
                    self.gentil = None
                    self.score -= 100
                if element.acteur.x < 0:
                    self.projectiles_H.remove(element)

        if self.gentil == None:
            self.gentil = Gentil()
        
        # Déplacement de l'hélicoptère.
        self.Helicoptere.choisirDirection(clavier)        
        self.Helicoptere.déplacer()
        

        self.score += 10



    def dessiner(self, ecran):
        """
        Fonction qui dessine sur l'écran les objets du jeu.

        Args:
            ecran (_type_): l'écran, ou la fenêtre en action.
        """
        ecran.clear()

        fond = "new_york.jpg"
        ecran.blit(fond, (0,0))

        self.gentil.dessiner()
        for terroriste in self.mechant:
            terroriste.dessiner()
        for missile in self.projectiles_A:
            missile.dessiner()
        for missile in self.projectiles_H:
            missile.dessiner()
        self.Tour.dessiner()
        self.tank.dessiner()
        self.Helicoptere.dessiner()

        if self.compteur_missile_temps >= 25:
            txt = "Chargé!"
        else:
            d = 25 - self.compteur_missile_temps 
            txt = f"{d} FPS restant."

        ecran.draw.text(f"Réserve de missile de tank : {str(self.compteur_missile_réserve)}     Hélicoptère : {txt}    Pointage : {self.score}", (10, 10), color="black")
        if self.game_over_HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE:
            ecran.draw.text("Les évènements du 9/11 se sont produit. Tu as perdu.", (275,290), color="black")
            self.compteur_fin += 1
            if self.compteur_fin == 2:
                self.Fin_de_parti()

    def Jouer_son_jeu(self, son):
        son.goose.play()

    def Fin_de_parti(self):
        """
        Envoi à controle.
        """
        self.controle = Controle(self.score)
        self.controle.Appelle_tk()
        
# Section de lancement du jeu.
jeu = Jeu()

def update():
    jeu.miseAJour(keyboard)

def draw():
    jeu.dessiner(screen)

pgzrun.go()