import csv

class LIRE_LE_NOMBRE_DE_LIGNE():
    """
    Renvoie le nonbre de ligne.
    """
    def AVOIR_LE_NBR_DE_LIGNE(self):
        with open("skill_issue.csv", mode="r", newline="", encoding="utf-8") as fichier:
            LEfichier = csv.reader(fichier, delimiter=";")
            x = 0
            for element in LEfichier:
                x += 1
            return x