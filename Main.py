import sys

import PySimpleGUI as py
from self import self

import formulario

py.theme("DarkGreen3")
def main():

    layout1 = [[ py.Text("Bem vindo ao sistema de cadastros Formtech",font="arial 14", )],
               [py.Text("")],
               [py.Text("Cadastros Disponiveis",font="arial 14")],
               [py.Button("Clientes", key="open", font="arial 12"),
                py.Button("Funcionarios",key='funci',font="arial 12"),
                py.Button("Produtos",key='prd',font="arial 12"),
                py.Button("Sair",key='Exit',font="arial 12",button_color="Red")
                ]]
    janela = py.Window("Login", layout1,size=(450,330))
    while True:
        event, values = janela.read()
        if event == "Exit" or event == py.WIN_CLOSED:
            break
        if event == "open":
            formulario.Formulario.init(self)

        if not event:
            break
        if event == 'Exit':
            sys.exit()
    janela.close()


if __name__ == "__main__":
    main()



