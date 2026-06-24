import sqlite3

def init_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Ativa o suporte a chaves estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Tabela de Usuários melhorada
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # 2. Tabela de Publicações (Produtos ou Notícias)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publication (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        type TEXT CHECK(type IN ('produto', 'noticia')) NOT NULL,
        price REAL, -- Opcional, usado se for produto
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
    )
    """)

    # Inserir dados de teste apenas se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM user")
    if cursor.fetchone()[0] == 0:
        # Nota: Em produção, NUNCA salve a senha em texto puro. Use Werkzeug ou bcrypt.
        cursor.execute("INSERT INTO user (nome, email, password) VALUES (?, ?, ?)", 
                       ("Marcos", "marcos@email.com", "senha123"))
        cursor.execute("INSERT INTO user (nome, email, password) VALUES (?, ?, ?)", 
                       ("Ana", "ana@email.com", "senha456"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    print("Banco de dados inicializado com sucesso!")