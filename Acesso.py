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
        self.titulo["font"] = self.fontePadrao
        self.titulo.pack()

        # LABEL NOME
        self.labelNome = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.labelNome.pack(side=LEFT)


        # Entry - Campo Nome
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)


        # LABEL SENHA
        self.labelSenha = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.labelSenha.pack(side=LEFT)

        # EXIBIÇÃO DA SENHA
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        # Botão para Acessar/ Autenticar
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Acessar"
        self.autenticar["font"] = ("Arial", "15")
        self.autenticar["width"] = 10
        self.autenticar["command"] = self.verificaSenha
        
        # verificaSenha é uma metodo que será passado para o command - linha 70

        # mensagem
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.autenticar.pack()

        # Método Verifica Senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        # validação
        # usuario e senha fictício
        if usuario == "user" and senha == "dev": 
            self.mensagem["text"] = "Autenticado" 
            self.mensagem.pack()
        else: 
            self.mensagem["text"] = "Erro na autenticação"
            self.mensagem.pack()



root = Tk()
Acesso(root)

# sem o evento loop a classe não será exibida

root.mainloop()