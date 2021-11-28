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
        clientes = [
                     ('Roberto','Jujubo','juro@gmail.com'),
                     ('Carol', 'Silva', 'casil@gmail.com'),
                     ('Godofredo', 'Silva', 'gosi@gmail.com'),
        ]
        self.c.executemany("INSERT INTO  clientes_loja VALUES(?,?,?)",clientes)

        self.conex.commit()
    def view_all(self):

        self.c.execute("SELECT * FROM  clientes_loja")

        self.view= self.c.fetchall()
        
        for item in self.view:
         print(item[0] + " " + item[1] + "\t\t " + item[2])

#Instancia a classe
banco_dados = Cadastro()
# Chama a funçao
banco_dados.view_all()