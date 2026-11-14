import pandas as pd
import matplotlib.pyplot as plt
import csv
from code_de_l_application_web.Mise_à_jour_du_fichier_csv import Mise_à_jour_du_fichier_csv


class PANDAS_PARCE_QUE():

    def __init__(self) -> None:
        liste = Mise_à_jour_du_fichier_csv().AVOIR_LISTE()
        with open("csv_pour_pandas.csv", mode="w", newline="", encoding="utf-8") as fichier:
            LAUTREfichier = csv.writer(fichier, delimiter=",")
            LAUTREfichier.writerow(["Id", "Score", "Nom", "Prenom", "Date_Heure"])
            LAUTREfichier.writerows(liste)

        self.dataframe = pd.read_csv("csv_pour_pandas.csv", encoding="utf-8")

        self.dataframe["Date_Heure"] = pd.to_datetime(self.dataframe["Date_Heure"])

        self.RegroupeMoy = self.dataframe.resample('M', on="Date_Heure").mean(numeric_only=True)
        self.RegroupeMax = self.dataframe.resample('M', on="Date_Heure").max()

        plt.plot(self.RegroupeMoy.index, self.RegroupeMoy["Id"], label="Id (moy. des gens qui ont joué)", color="red")
        plt.plot(self.RegroupeMoy.index, self.RegroupeMoy["Score"], label="Score (moy)", color="blue")
        plt.plot(self.RegroupeMax.index, self.RegroupeMax["Id"], label="Id (Nbr de gens total qui ont joué)", color="darkred")
        plt.plot(self.RegroupeMax.index, self.RegroupeMax["Score"], label="Score (max)", color="darkblue")

        plt.xlabel("f")
        plt.ylabel("ff")
        plt.title("Leaderboard")
        plt.legend()

        plt.show()
