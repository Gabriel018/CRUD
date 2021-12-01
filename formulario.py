import PySimpleGUI as py

import database
from database import *


class Self:
    pass


class Formulario():

    def __init__(self):

        self.layout = [[py.Text("Nome"), py.Input(key='name')],
                       [py.Text("Sobrenome"), py.Input(key='name_sobre')],
                       [py.Text("Email"), py.Input(key='Email')],
                       [py.Button("Cadastrar", key='add')]
                       ]

    def Init(self):

        self.janela = py.Window("Fomurlario de clientes", self.layout, size=(400, 300))

        while True:

            self.event, self.values = self.janela.read()

            if self.event == "add":
                Nome = self.values['name']
                Sobre_Nome = self.values['name_sobre']
                Email = self.values['Email']

                database.add_clientes(self,Nome, Sobre_Nome, Email)
                self.janela.find_element('name').update('')
                self.janela.find_element('name_sobre').update('')
                self.janela.find_element('Email').update('')

                py.popup("Cadastrado com sucesso")



Form = Formulario()
Form.__init__()
Form.Init()

