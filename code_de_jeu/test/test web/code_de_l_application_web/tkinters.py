import tkinter
import datetime
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import messagebox
from tkinter import Button
from tkinter import ttk
from tkinter import Entry
from code_de_l_application_web.Append_nouveau_résultats import Append
from code_de_l_application_web.LIRE_LE_NOMBRE_DE_LIGNE import LIRE_LE_NOMBRE_DE_LIGNE
from code_de_l_application_web.Mise_à_jour_du_fichier_csv import Mise_à_jour_du_fichier_csv
from code_de_l_application_web.PANDAS import PANDAS_PARCE_QUE

class Tkinter():

    """
    crée le pop up du menu
    """
    def __init__(self, score) -> None:
        self.fenêtre = Tk()
        self.fenêtre.title("")
        self.fenêtre.geometry("400x250")
        self.fenêtre.config(bg="white")

        self.lbl_nom = Label(self.fenêtre, text="Nom")
        self.lbl_nom.place(x=5,y=10)

        self.txt_nom = Entry(self.fenêtre, width=10, font="Calibri 20")
        self.txt_nom.place(x=60,y=10)

        self.lbl_prenom = Label(self.fenêtre, text="Prenom")
        self.lbl_prenom.place(x=5,y=60)

        self.txt_prenom = Entry(self.fenêtre, width=10, font="Calibri 20")
        self.txt_prenom.place(x=60,y=60)

        self.btn_envoyer = Button(self.fenêtre, text="Envoyer les résultats au lederboard", command=lambda:self.config_append())
        self.btn_envoyer.place(x=80,y=110)

        self.btn_leader = Button(self.fenêtre, text="Leaderboard", command=lambda:self.Appelle_app())
        self.btn_leader.place(x=80,y=150)

        self.btn_pandas = Button(self.fenêtre, text="Pandas", command=lambda:PANDAS_PARCE_QUE())
        self.btn_pandas.place(x=80,y=210)

        self.score = score
        
    def run(self):
        """
        Ouvre la fenêtre.
        """
        self.fenêtre.mainloop()

    def config_append(self):
        """
        Append.
        """
        self.btn_envoyer.config(state="disabled")
        self.id = LIRE_LE_NOMBRE_DE_LIGNE().AVOIR_LE_NBR_DE_LIGNE()
        if self.id == 0:
            v = datetime.datetime.today()
            p = str(v)
            i = 0
            if p[5] == "1":
                i += 10
            else:
                i += int(p[6])
            i -= 1
            v = datetime.date.replace(v, month=i)
            Append().Append_score(0, 10000, "du serveur", "bot", str(v))
        d = d = str(datetime.date.today())
        self.nom = self.txt_nom.get()
        self.prenom = self.txt_prenom.get()
        Append().Append_score(self.id, self.score, self.nom, self.prenom, d)
        Mise_à_jour_du_fichier_csv().Mise_à_jour_du_fichier_csv_frame()

    def Appelle_app(self):
        """
        Appelle l'aplication web.
        """
        messagebox.showwarning("ATTENTION CAUSEUR DE 9/11!!", "CONTINUER VA DELETE VOTRE PARTI.")
        self.fenêtre.destroy()
        messagebox.showinfo("Adresse pour leaderboard :", "http://127.0.0.1:5000")

        from code_de_l_application_web.app import App
        self.flask = App(__name__)
        self.flask.runs()
