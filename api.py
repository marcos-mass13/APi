from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
# from flask_mysqldb import MySQL
import pymysql
import sqlite3
import subprocess

# Executa o outro arquivo e espera ele terminar
subprocess.run(["python", "arquivo.py"])
print("O outro arquivo terminou de rodar! Continuando este script...")
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

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM noticias")
    noticias = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM produtos")
    produtos = [dict(row) for row in cursor.fetchall()]

    conn.close()

    print(produtos)
    return jsonify({
            "mensagem": "API ativa e banco preparado!",
            "noticias": noticias,
            "produtos": produtos
        })


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

@app.route('/usuarios', methods=['POST'])
def listar_todos_usuarios():
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
    

    
# Rota para buscar um usuário por ID
@app.route('/noticias')
def listar_todos_noticias():
         conn = conectar()
         cursor = conn.cursor()

         cursor.execute("SELECT * FROM noticias")
         noticias = [dict(row) for row in cursor.fetchall()]

         return jsonify({
            "mensagem": "Consulta realizada!",
            "noticias": noticias,
            }) 
      
      

@app.route('/noticias/<int:id>', methods=['GET'])
def find_noticias(id):
      try:
        print("dont here")
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM noticias WHERE id = ?", (id,))
        noticias = cursor.fetchone()

        conn.close()

        return jsonify(dict(noticias))
      
      except Exception as e:
        return jsonify({"erro": str(e)})
      

@app.route('/noticias', methods=['POST'])
def criar_noticias():
      try:
        conn = conectar()
        cursor = conn.cursor()

        dados = request.get_json()

        title = dados.get('title')
        content = dados.get('content') 
        usuario_id = dados.get('usuario_id')

        cursor.execute("INSERT INTO noticias (title, content, usuario_id) VALUES (?,?,?)",(title, content, usuario_id))

        conn.commit()
        conn.close()
        return jsonify({
            "mensagem": "Cadastro realizado com sucesso"
        })
      
      except Exception as e:
        return jsonify({"erro": str(e)})



   
# Rota para buscar um usuário por ID
@app.route('/produtos')
def listar_todos_produtos():
      
      conn = conectar()
      cursor = conn.cursor()

      cursor.execute("SELECT * FROM produtos")
      produtos = [dict(row) for row in cursor.fetchall()]

      return jsonify({
          "mensagem": "Consulta realizada!",
          "produtos": produtos
      })
      

@app.route('/produtos/<int:id>', methods=['GET'])
def find_produtos(id):
      try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
        produtos = cursor.fetchone()

        conn.close()

        return jsonify(dict(produtos))
      
      except Exception as e:
        return jsonify({"erro": str(e)})
      

@app.route('/produtos', methods=['POST'])
def criar_produtos():
      try:
        conn = conectar()
        cursor = conn.cursor()

        dados = request.get_json()

        title = dados.get('title')
        content = dados.get('content') 
        price = dados.get('price')
        usuario_id = dados.get('usuario_id')

        cursor.execute("INSERT INTO produtos (title, content, price, usuario_id)VALUES (?,?,?,?)",(title, content, price, usuario_id))
        

        conn.commit()
        conn.close()

        return jsonify({
            "mensagem": "Cadastro realizado com sucesso"
        })
      
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