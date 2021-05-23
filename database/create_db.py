import sqlite3

data_base = "data_base1"

banco = sqlite3.connect(data_base)
cursor = banco.cursor()

cursor.execute("CREATE TABLE ")