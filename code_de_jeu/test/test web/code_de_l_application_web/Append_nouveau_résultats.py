import csv

class Append():
    
    """
    Apprend un résultat.
    """
    def Append_score(self, id, score, nom, prenom, d):
        with open("skill_issue.csv", mode="a", encoding="utf-8", newline="") as fichier:
            LEfichier = csv.writer(fichier, delimiter=";")
            LEfichier.writerow([id, score, nom, prenom, d])
            liste = [id, score, nom, prenom, d]
            