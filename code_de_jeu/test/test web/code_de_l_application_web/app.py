from flask import Flask, render_template
from code_de_l_application_web.voir_liste_stats import Voir_liste_stats
from code_de_l_application_web.supprimer import SupprimerJoueur
from code_de_l_application_web.EditerContact import EditerContact

class App():
    
    """
    Initie la class de l'application web.
    """
    def __init__(self, Nom) -> None:
        """
        Crée les routes de l'application web.
        """
        self.app = Flask(Nom)
        self.routes()
    
    
    def routes(self):
        self.app.add_url_rule('/', view_func=Voir_liste_stats.as_view("afficher_liste_contact"))
        self.app.add_url_rule("/modifié/<int:identifiant>/", view_func=EditerContact.as_view("editer"), methods=["GET", "POST"])
        self.app.add_url_rule("/retirer/<int:identifiant>/", view_func=SupprimerJoueur.as_view("supprimer"), methods=["GET", "POST"])
    

    def runs(self):
        """
        exexute l'application
        """
        self.app.run()

