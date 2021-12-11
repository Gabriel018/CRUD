import sqlite3


def creat_table(self):
            self.conex = sqlite3.connect("clientes.db")
            self.c = self.conex.cursor()

            self.c.execute("""CREATE TABLE  clientes_loja(
                              Nome text,
                              Sobre_Nome text,
                              Email text,,                        
            )""")

def add_clientes(self,Nome,Sobre_Nome,Email):
            self.conex = sqlite3.connect("clientes.db")
            self.c = self.conex.cursor()

            self.c.execute("INSERT INTO  clientes_loja VALUES(?,?,?)",(Nome,Sobre_Nome ,Email))

            self.conex.commit()

def update(self,Nome,Sobre_Nome,Email):
           self.conex = sqlite3.connect("clientes.db")
           self.self.c.execute(" UPDATE  clientes_loja SET Nome =? WHERE  Nome =? ",(Nome,Sobre_Nome ,Email))

           self.conex.commit()

def delete(self,x):
          # quando o tipo de dado for invalido add, "(str(data[0]), )"
          self.conex = sqlite3.connect("clientes.db")
          self.c = self.conex.cursor()
          self.c.execute(" DELETE FROM clientes_loja WHERE Nome=?",(str(x[0]),))

          self.conex.commit()






def view_all(self):
            self.conex = sqlite3.connect("clientes.db")
            self.c = self.conex.cursor()

            self.c.execute("SELECT * FROM  clientes_loja")

            self.view= self.c.fetchall()

        #    for item in self.view:


            return self.view




