from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
# from flask_mysqldb import MySQL
import pymysql
import sqlite3
#teste deploy
app = Flask(__name__)
CORS(app)

# Função para conectar ao banco
def conectar():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

# teste inicio
def new_conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',       # Padrão do XAMPP é sem senha
        database='nome_do_seu_banco', # Mude para o seu banco
        port=3306,
        cursorclass=pymysql.cursors.DictCursor # Faz os resultados virem como dicionário (chave: valor)
    )
# teste inicio

@app.route("/")
def home():
    # redirect(url_for('https://teste-eta-opal-50.vercel.app/'))
    return jsonify({
            "mensagem": "API ativa e banco preparado!"
        })
    # return redirect('https://teste-eta-opal-50.vercel.app/')

# Manipulador global para erro 404
@app.errorhandler(404)
def tratar_404(error):
    return redirect('https://teste-eta-opal-50.vercel.app/')


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

@app.route('/user', methods=['POST'])
def listar_todos_usuarios():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user")
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