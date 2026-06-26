import sqlite3

def init_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # IMPORTANTE: Ativa o suporte a chaves estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Tabela de Usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # 2. Nova Tabela de Noticias (Sem campo de preço e sem coluna type)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS noticias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        usuario_id INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    )
    """)

    # 3. Nova Tabela de Produtos (Preço agora é obrigatório NOT NULL)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        price REAL NOT NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        usuario_id INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    )
    """)

    # Inserir dados de teste iniciais se a tabela 'usuarios' estiver vazia
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (nome, email, password) VALUES (?, ?, ?)", 
                       ("Marcos", "marcos@email.com", "senha123"))
        cursor.execute("INSERT INTO usuarios (nome, email, password) VALUES (?, ?, ?)", 
                       ("Ana", "ana@email.com", "senha456"))
        
        # Guardando os IDs inseridos para criar os relacionamentos de teste

        # Inserindo dados de teste diretamente nas novas tabelas separadas
        cursor.execute("INSERT INTO noticias (title, content, usuario_id) VALUES (?, ?, ?)",
                       ("Novidades no Desenvolvimento Vue 4", "Confira as atualizações de performance estruturais.", 1))
        
        cursor.execute("INSERT INTO produtos (title, content, price, usuario_id) VALUES (?, ?, ?, ?)",
                       ("Câmera Mirrorless Pro 2", "Sensor full-frame de alta resolução.", 277.00, 2))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    print("Banco de dados [OK]!")