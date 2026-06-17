


import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

# Inserir dados de teste
cursor.execute("INSERT INTO user (nome, email) VALUES (?, ?)", ("Marcos", "marcos@email.com"))
cursor.execute("INSERT INTO user (nome, email) VALUES (?, ?)", ("Ana", "ana@email.com"))

conn.commit()
conn.close()