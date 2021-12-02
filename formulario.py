import PySimpleGUI as py
import self as self

import database
from database import *


class Self:
    pass


class Formulario():

    def __init__(self,):
        clientes_view = database.view_all(self)
        self.layout = [ [ py.Text("Cadastro de Clientes",font="arianl 16",text_color='black',justification = 'center')],
                       [py.Text("Nome:",font="arial 14",text_color="black",),py.Input(size=(40,1),key='name'),],
                       [py.Text("Sobrenome:",font="arial 14",text_color="black",),py.Input(size=(40,2),key='name_sobre')],
                       [py.Text("Email:",font="arial 14",text_color="black"), py.Input(size=(40,2),key='Email')],
                       [py.Button("Cadastrar", key='add',font="arial 12"),
                        py.Button("Alterar", key='alter',font="arial 12"),
                        py.Button("Deletar", key='del',font="arial 12")],
                        [py.Text("Lista de Clientes",font="arianl 16",text_color='black')],
                        [py.Listbox(clientes_view,size=(50,10),key='Box',font='arial')  ]]

    def Init(self):

        self.janela = py.Window("Fomurlario de clientes", self.layout, size=(600, 500))

        while True:

            self.event, self.values = self.janela.read()
            if self.event == py.WIN_CLOSED or self.event == 'Cancel':  # if user closes window or clicks cancel
                break

            if self.event == "add":
                Nome = self.values['name']
                Sobre_Nome = self.values['name_sobre']
                Email = self.values['Email']
                clientes_view = database.view_all(self)
                database.add_clientes(self,Nome, Sobre_Nome, Email)

                self.janela.find_element('name').update('')
                self.janela.find_element('name_sobre').update('')
                self.janela.find_element('Email').update('')
                self.janela.find_element('Box').update(clientes_view)

                py.popup("Cadastrado com sucesso")
            if self.event == "del":
                x = self.values['Box'][0]
                database.delete(self,x)
                clientes_view = database.view_all(self)
                self.janela.find_element('Box').update(clientes_view)

Form = Formulario()
Form.__init__()
Form.Init()

