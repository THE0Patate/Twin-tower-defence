import csv

class Mise_à_jour_du_fichier_csv():
    """
    La classe pour géger le csv.
    """

    def Mise_à_jour_du_fichier_csv_frame(self):
        """
        Met à jour la liste.
        """
        liste = self.AVOIR_LISTE()
        with open("skill_issue.csv", mode="w", newline="", encoding="utf-8") as fichier:
            LEfichier = csv.writer(fichier, delimiter=";")
            for element in liste:
                x = 0
                if len(liste) > 1:
                    for nbr in range(len(liste)):
                        if element[1] < liste[nbr][1]:
                            x += 1
                    element[0] = x
                LEfichier.writerow(element)
        self.classement()

    def AVOIR_LISTE(self):
        """
        Renvoi la liste du cvs.
        Returns:
            _type_: list
        """
        with open("skill_issue.csv", mode="r", newline="", encoding="utf-8") as fichier:
            LEfichier = csv.reader(fichier, delimiter=";")
            liste = []
            for element in LEfichier:
                liste.append([int(element[0]), int(element[1]), str(element[2]), str(element[3]), str(element[4])])
            return liste
        
    def Mise_à_jour_du_fichier_csv_sur_demande(self, liste_joueur):
        """
        Réécrit le ficier csv sur demande.
        """
        liste = self.AVOIR_LISTE()
        with open("skill_issue.csv", mode="w", newline="", encoding="utf-8") as fichier:
            LEfichier = csv.writer(fichier, delimiter=";")
            liste[liste_joueur[0]] = liste_joueur
            LEfichier.writerows(liste)

    def SUPRIMER_TON_SKILL_ISSUE(self, liste_joueur):
        """
        Supprime un joueur de la liste.
        Args:
            liste_joueur (_type_): liste
        """
        liste = self.AVOIR_LISTE()
        
        with open("skill_issue.csv", mode="w", newline="", encoding="utf-8") as fichier:
            LEfichier = csv.writer(fichier, delimiter=";")
            liste.pop(liste_joueur[0])
            LEfichier.writerows(liste)

    def classement(self):
        """
        Classe les scores en ordre de skill.
        """
        liste = self.AVOIR_LISTE()
        with open("skill_issue.csv", mode="w", newline="", encoding="utf-8") as fichier:
            LEfichier = csv.writer(fichier, delimiter=";")
            liste.sort()
            LEfichier.writerows(liste)
                    