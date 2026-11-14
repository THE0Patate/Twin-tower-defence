import csv
from code_de_l_application_web.Mise_à_jour_du_fichier_csv import Mise_à_jour_du_fichier_csv

class Aller_chercher_joueur_via_id():

    def Aller_chercher_joueur_via_id(self, id):
        liste = Mise_à_jour_du_fichier_csv().AVOIR_LISTE()
        return liste[id]
            