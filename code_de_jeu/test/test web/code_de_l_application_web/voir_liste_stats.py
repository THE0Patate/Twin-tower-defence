from flask import render_template
from flask.views import View
from code_de_l_application_web.Mise_à_jour_du_fichier_csv import Mise_à_jour_du_fichier_csv


class Voir_liste_stats(View):
    
    def dispatch_request(self) -> str: 
        liste = Mise_à_jour_du_fichier_csv().AVOIR_LISTE()
        return render_template("structure.html", liste_statistiques=liste)
