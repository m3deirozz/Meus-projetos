import sqlite3





conn = sqlite3.connect("recursos.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS recursos(

  id INTEGER PRIMARY KEY AUTOINCREMENT,

  produto TEXT NOT NULL,

  quantidade INTEGER NOT NULL,

  tipo TEXT NOT NULL,

  consumo INTEGER NOT NULL DEFAULT 0,

  producao_diaria INTEGER NOT NULL DEFAULT 0

)

""")

conn.commit()



dados = [

  ('Ferro', 41, 'entrada'),

  ('Estaca', 0, 'entrada'),

  ('Alimentos', 120, 'entrada'),

  ('Alimentos', 30, 'saida')

]

cursor.executemany("INSERT INTO recursos (produto, quantidade, tipo) VALUES (?, ?, ?)", dados)

conn.commit()



cursor.execute("SELECT * FROM recursos")



for linha in cursor.fetchall():

  print(linha)
