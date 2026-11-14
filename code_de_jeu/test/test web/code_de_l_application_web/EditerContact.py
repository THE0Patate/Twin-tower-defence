from flask import render_template, request
from flask.views import View
from code_de_l_application_web.Aller_chercher_joueur_via_id import Aller_chercher_joueur_via_id
from code_de_l_application_web.Mise_à_jour_du_fichier_csv import Mise_à_jour_du_fichier_csv

class EditerContact(View):

    """
    Fonction qui permet de modifier un des contact (le prenom) et le (nom)
    """
    def dispatch_request(self, identifiant: int) -> str:

        contact_en_cours = Aller_chercher_joueur_via_id().Aller_chercher_joueur_via_id(identifiant)

        if request.method == "POST":

            nom_saisi = request.form["nom"].strip()
            prenom_saisi = request.form["prenom"].strip()

            if len(nom_saisi) < 3 or len(prenom_saisi) < 3:
                erreur = "PasValide"
                return render_template("formulaire.html", contact=contact_en_cours, erreur=erreur)
            else:
                contact_en_cours[2] = nom_saisi
                contact_en_cours[3] = prenom_saisi
                Mise_à_jour_du_fichier_csv().Mise_à_jour_du_fichier_csv_sur_demande(contact_en_cours)

        return render_template("formulaire.html", contact=contact_en_cours)
            

