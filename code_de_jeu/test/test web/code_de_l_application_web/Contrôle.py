from code_de_l_application_web.tkinters import Tkinter

class Controle():

    def __init__(self, score) -> None:
        self.tkinter = Tkinter(score)
        
    def Appelle_tk(self):    
        self.tkinter.run()