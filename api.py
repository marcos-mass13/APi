from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Função para conectar ao banco
def conectar():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

# Rota para listar dados
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        # Converter para lista de dicionários
        resultado = [dict(usuario) for usuario in usuarios]

        conn.close()

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)})

# Rota para buscar um usuário por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        usuario = cursor.fetchone()

        conn.close()

        if usuario:
            return jsonify(dict(usuario))
        else:
            return jsonify({"mensagem": "Usuário não encontrado"})

    except Exception as e:
        return jsonify({"erro": str(e)})
    
# CADASTRO
@app.route('/cadastro', methods=['POST'])
def cadastro():

    try:
        dados = request.get_json()

        nome = dados.get('nome')
        email = dados.get('email')
        senha = dados.get('senha')

        print(nome)
        print(email)
        print(senha)

        return jsonify({
            "mensagem": "Cadastro recebido com sucesso",
            "dados": dados
        })

    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == '__main__':
    app.run(debug=True)