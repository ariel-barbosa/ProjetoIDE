import tkinter
from tkinter import *

class Acesso:

    def __init__(self, master=None):

        # confg do frame
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        # segundo container
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        # terceiro container
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        # quarto container
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        # LABEL TITULO
        self.titulo = Label(self.primeiroContainer, text="LOGIN")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()

        # LABEL NOME
        self.labalNome = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.labalNome.pack(side=LEFT)

        # Entry - Campo Nome
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)



root = Tk()
Acesso(root)

# sem o evento loop a classe não será exibida

root.mainloop()