# Tkinter é a biblioteca padrão do Python para
# criar interfaces gráficas de usuário (GUI).
# Com Tkinter, os desenvolvedores podem criar
# janelas, botões, caixas de entrada, menus e
# outros componentes gráficos de forma simples
# e eficiente.

import tkinter
from tkinter import *


class Aplicativo:
    def __init__(self, master=None):
        # self.mudarTexto = None
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Arial", "14", "bold")
        self.msg.pack(side=RIGHT)

        # botão SAIR
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique Aqui"
        self.sair["font"] = ("Arial", "20")
        self.sair["width"] = 10
        # self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair["command"] = self.mudarTexto
        self.sair.pack(side=TOP)

        # mensagem que aparece ao clicar no botão
    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "clicado"
        else:
            self.msg["text"] = "Primeiro widget"


root = Tk()
Aplicativo(root)

# sem o evento loop a classe não será exibida

root.mainloop()
