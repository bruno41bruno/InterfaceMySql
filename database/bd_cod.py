""" import sqlite3

parametro = "cliente = bruno"

filtro = "cliente"

banco = sqlite3.connect("data_base")
cursor = banco.cursor()

cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall()) """



#criarTabela
""" cursor.execute("CREATE TABLE clientes (nome text, data text, operacao text, valor_total text, valor_cambio text, valor_original text)") """



#inserir
""" cursor.execute("Insert INTO clientes VALUES("'"+data+"','"+nome+"','"+operacao+"','"+valor_total+"','"+valor_cambio+"','"+valor_original+"')
banco.commit() """


#deletar
""" cursor.execute("DELETE FROM clientes WHERE '"+parametro+"'")

    cursor.execute()
    banco.commit() """

#filtro
""" cursor.execute("SELECT * FROM clientes WHERE '"+parametro+"'")
print(cursor.fetchall())

banco.commit()
banco.close()

banco.row_factory = sqlite3.Row

for row in cursor.execute("SELECT rowid, * FROM clientes ORDER BY '"+filtro+"'"):
    print(row) """
    

""" except sqlite3.Error as erro:
    print("fail") """