import os
import unittest
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import messagebox
from tkinter import Button
from tkinter import ttk
from tkinter import Entry

class Tkinter(unittest.TestCase):
    
    def __init__(self) -> None:
        self.fenêtre = Tk()
        self.fenêtre.title("")
        self.fenêtre.geometry("200x200")
        self.fenêtre.config(bg="white")

        self.txt_nom = Entry(self.fenêtre, width=3, font="Calibri 20")
        self.txt_nom.place(x=100,y=10)

        self.run()
        
    def run(self):
        self.fenêtre.mainloop()