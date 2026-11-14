from flask import render_template
from flask.views import View
from code_de_l_application_web.Aller_chercher_joueur_via_id import Aller_chercher_joueur_via_id
from code_de_l_application_web.Mise_à_jour_du_fichier_csv import Mise_à_jour_du_fichier_csv

class SupprimerJoueur(View):
    """
    va chercher les fonction qui permet de suprimer un joyueur de la liste de scores. 
    Args:
        View (_type_): _description_
    """

    def dispatch_request(self, identifiant: int) -> str:

        Joueur = Aller_chercher_joueur_via_id().Aller_chercher_joueur_via_id(identifiant)

        Mise_à_jour_du_fichier_csv().SUPRIMER_TON_SKILL_ISSUE(Joueur)

        return render_template("fin.html")