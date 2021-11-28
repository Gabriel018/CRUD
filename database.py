import sqlite3



class  Cadastro():

    def __init__(self):
        self.conex = sqlite3.connect("clientes.db")
        self.c = self.conex.cursor()

    def creat_table(self):
        self.c.execute("""CREATE TABLE  clientes_loja(
                          Nome text,
                          Sobre_Nome text,
                          Email text,,                        
        )""")


    def add_clientes(self):

        self.c.execute("INSERT INTO  clientes_loja VALUES('Adalberto','Soares','adal@.com')")

        self.conex.commit()


#Instancia a classe
banco_dados = Cadastro()
# Chama a funçao
banco_dados.add_clientes()