# app.py
from flask import Flask, render_template, jsonify, request
from dao import UsuarioDAO

app = Flask(__name__, static_url_path='/static')
usuario_dao = UsuarioDAO()

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/insert', methods=['POST'])
def insert_usuario():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    try:
        usuario_dao.inserir_usuario(email, senha)
        return jsonify({'message': 'Cadastro realizado com sucesso!'}), 200
    except Exception as e:
        print("Erro ao inserir dados:", e)
        return jsonify({'error': 'Ocorreu um erro ao cadastrar o usuário.'}), 500

@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    if usuario_dao.validar_credenciais(email, senha):
        return jsonify({'message': 'Login bem-sucedido!'}), 200
    else:
        return jsonify({'error': 'Credenciais inválidas. Por favor, verifique seu email e senha.'}), 401

# Rotas adicionais
@app.route('/Cadastre-se.html')
def cadastrese():
    return render_template('cadastre-se.html')

@app.route('/FAQ.html')
def FAQ():
    return render_template('FAQ.html')

@app.route('/contact.html')
def contato():
    return render_template('contact.html')

@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@app.route('/secondPage.html')
def secondPage():
    return render_template('secondPage.html')

@app.route('/index1/applevision.html')
def applevision():
    return render_template('index1/applevision.html')

@app.route('/index1/iphone.html')
def iphone():
    return render_template('index1/iphone.html')

@app.route('/index1/fone.html')
def fone():
    return render_template('index1/fone.html')

@app.route('/index1/gabinete.html')
def gabinete():
    return render_template('index1/gabinete.html')

@app.route('/index1/teclado.html')
def teclado():
    return render_template('index1/teclado.html')

@app.route('/index1/mouse.html')
def mouse():
    return render_template('index1/mouse.html')

@app.route('/index1/SSD.html')
def SSD():
    return render_template('index1/SSD.html')

@app.route('/index1/xioami.html')
def xioami():
    return render_template('index1/xioami.html')
    
@app.route('/index1/tecladorazer.html')
def tecladorazer():
    return render_template('index1/tecladorazer.html')

@app.route('/index1/placamae.html')
def placamae():
    return render_template('index1/placamae.html')

@app.route('/index1/rtx4090.html')
def rtx4090():
    return render_template('index1/rtx4090.html')

@app.route('/index1/alexa.html')
def alexa():
    return render_template('index1/alexa.html')

@app.route('/index2/monitor.html')
def monitor():
    return render_template('index2/monitor.html')

@app.route('/index2/ps5.html')
def ps5():
    return render_template('index2/ps5.html')

@app.route('/index2/xbox.html')
def xbox():
    return render_template('index2/xbox.html')

@app.route('/index2/controleps5.html')
def controleps5():
    return render_template('index2/controleps5.html')

@app.route('/index2/controlexbox.html')
def controlexbox():
    return render_template('index2/controlexbox.html')

@app.route('/index2/watercoller.html')
def watercoller():
    return render_template('index2/watercoller.html')

# E assim por diante...

if __name__ == "__main__":
    app.run(debug=True)
