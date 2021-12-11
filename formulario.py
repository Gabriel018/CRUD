import sys

import PySimpleGUI as py
import self as self

import database
from database import *

py.theme("DarkGreen3")
class Self:
    pass


class Formulario():

    def init(self):
        clientes_view = database.view_all(self)



        self.layout2 = [ [ py.Text("Cadastro de Clientes",font="arianl 16",justification = 'c')],
                        [py.Text("Nome:",font="arial 14",justification='c')],
                        [py.Input(size=(40,1),key='name'),],
                        [py.Text("Sobrenome:",font="arial 14",)],
                        [py.Input(size=(40,2),key='name_sobre')],
                        [py.Text("Email:",font="arial 14",)],
                        [py.Input(size=(40,2),key='Email')],
                        [py.Button("Cadastrar", key='add',font="arial 12"),
                        py.Button("Alterar", key='alt', font="arial 12"),
                        py.Button("Deletar", key='del',font="arial 12")],
                        [py.Text("Lista de Clientes",font="arianl 16")],
                        [py.Listbox(clientes_view, size=(50,10), enable_events=True, key='Box', font='arial')] ,
                        [py.Button("Voltar",key="back",font="arial 12"), py.Button("sair",key="exit",font="arial 12")]]



        self.janela = py.Window("Fomurlario de clientes", self.layout2, size=(600, 550))

        while True:
            clientes_view = database.view_all(self)
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
                clientes_view = database.view_all(self)
            if self.event == "alt":
                x = self.values['Box'][0]
                Nome = self.values['name']
                Sobre_Nome = self.values['name_sobre']
                Email = self.values['Email']
                self.janela.find_element('name').update(x[0])
                self.janela.find_element('name_sobre').update(x[1])
                self.janela.find_element('Email').update(x[2])
                database.update(self, Nome, Sobre_Nome, Email)
               # database.delete(self, x)

                clientes_view = database.view_all(self)
                self.janela.find_element('Box').update(clientes_view)
                print(x)


                py.popup("Cadastrado com sucesso")
            if self.event == "del":
                x = self.values['Box'][0]
                database.delete(self,x)
                clientes_view = database.view_all(self)
                self.janela.find_element('Box').update(clientes_view)
                print(x)
            if self.event == "exit":
                sys.exit()


