import sqlite3

def init_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # IMPORTANTE: Ativa o suporte a chaves estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Tabela alterada para 'usuarios'
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # 2. Tabela de Publicações corrigida para apontar para 'usuarios(id)'
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publication (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        type TEXT CHECK(type IN ('produto', 'noticia')) NOT NULL,
        price REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        usuario_id INTEGER NOT NULL, -- Nome ajustado para manter o padrão
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    )
    """)

    # Inserir dados de teste apenas se a tabela 'usuarios' estiver vazia
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (nome, email, password) VALUES (?, ?, ?)", 
                       ("Marcos", "marcos@email.com", "senha123"))
        cursor.execute("INSERT INTO usuarios (nome, email, password) VALUES (?, ?, ?)", 
                       ("Ana", "ana@email.com", "senha456"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    print("Banco de dados atualizado para 'usuarios' com sucesso!")