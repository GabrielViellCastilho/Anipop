from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_mysqldb import MySQL
import requests
import MySQLdb


app = Flask("__name__")


app.secret_key = "12345678"

app.config['MYSQL_HOST'] = 'localhost' #'127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'GabrielViell'
app.config['MYSQL_DB'] = 'BD_Anipop'
mysql = MySQL(app)

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route("/")
def home():

    Nome_Inteiro_Logado = session.get('Nome_Usuario_Logado')
    if session.get('Nome_Usuario_Logado'):
        Nome_Logado = session.get('Nome_Usuario_Logado').split()[0]
    else:
        Nome_Logado = None
    
    ID_Logado = session.get('ID_Usuario_Logado')
    Email_Logado = session.get ('Email_Usuario_Logado')
    Data_Logado = session.get ('Data_Usuario_Logado')
    Imagem_Usuario_Logado = session.get('Imagem_Usuario_Logado')
    return render_template("index.html",ID_Logado=ID_Logado, Nome_Inteiro_Logado = Nome_Inteiro_Logado,  Nome_Logado=Nome_Logado,  Email_Logado = Email_Logado, Data_Logado=Data_Logado, Imagem_Usuario_Logado = Imagem_Usuario_Logado)

@app.route("/A_Ascensão_de_Thanos_Marvel_Essenciais_Capa_dura")
def A_Ascensão_de_Thanos_Marvel_Essenciais_Capa_dura():
    Nome_Inteiro_Logado = session.get('Nome_Usuario_Logado')
    if session.get('Nome_Usuario_Logado'):
        Nome_Logado = session.get('Nome_Usuario_Logado').split()[0]
    else:
        Nome_Logado = None
    
    ID_Logado = session.get('ID_Usuario_Logado')
    Email_Logado = session.get ('Email_Usuario_Logado')
    Data_Logado = session.get ('Data_Usuario_Logado')
    Imagem_Usuario_Logado = session.get('Imagem_Usuario_Logado')
    return render_template("A_Ascensão_de_Thanos_Marvel_Essenciais_Capa_dura.html",ID_Logado=ID_Logado, Nome_Inteiro_Logado = Nome_Inteiro_Logado,  Nome_Logado=Nome_Logado,  Email_Logado = Email_Logado, Data_Logado=Data_Logado, Imagem_Usuario_Logado = Imagem_Usuario_Logado)

@app.route("/Mangas")
def Mangas():

    Nome_Inteiro_Logado = session.get('Nome_Usuario_Logado')
    if session.get('Nome_Usuario_Logado'):
        Nome_Logado = session.get('Nome_Usuario_Logado').split()[0]
    else:
        Nome_Logado = None
    
    ID_Logado = session.get('ID_Usuario_Logado')
    Email_Logado = session.get ('Email_Usuario_Logado')
    Data_Logado = session.get ('Data_Usuario_Logado')
    Imagem_Usuario_Logado = session.get('Imagem_Usuario_Logado')
    return render_template("mangas.html",ID_Logado=ID_Logado, Nome_Inteiro_Logado = Nome_Inteiro_Logado,  Nome_Logado=Nome_Logado,  Email_Logado = Email_Logado, Data_Logado=Data_Logado, Imagem_Usuario_Logado = Imagem_Usuario_Logado)

@app.route("/Mangas2")
def Mangas2():
    Nome_Inteiro_Logado = session.get('Nome_Usuario_Logado')
    if session.get('Nome_Usuario_Logado'):
        Nome_Logado = session.get('Nome_Usuario_Logado').split()[0]
    else:
        Nome_Logado = None
    
    ID_Logado = session.get('ID_Usuario_Logado')
    Email_Logado = session.get ('Email_Usuario_Logado')
    Data_Logado = session.get ('Data_Usuario_Logado')
    Imagem_Usuario_Logado = session.get('Imagem_Usuario_Logado')
    return render_template("mangas2.html",ID_Logado=ID_Logado, Nome_Inteiro_Logado = Nome_Inteiro_Logado,  Nome_Logado=Nome_Logado,  Email_Logado = Email_Logado, Data_Logado=Data_Logado, Imagem_Usuario_Logado = Imagem_Usuario_Logado)


@app.route("/Login", methods=['POST'])
def Login():
    Login_Dados = request.get_json()
    Email = Login_Dados.get("Email")
    Senha = Login_Dados.get('Senha')
    Email_Encontrado = None


    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT u.UsuarioID, u.Nome, u.Email, u.Senha, u.DataCriacao, a.Caminho_Imagem FROM Usuarios u JOIN Avatar a ON u.AvatarID = a.AvatarID WHERE u.Email = %s;", (Email,))
        Usuario = cur.fetchone()
        cur.close()


        if Usuario and Usuario[3]==Senha:
            session['ID_Usuario_Logado'] = Usuario[0]
            session['Nome_Usuario_Logado'] = Usuario[1]
            session['Email_Usuario_Logado'] = Usuario[2]
            session['Data_Usuario_Logado'] = Usuario[4]
            session['Imagem_Usuario_Logado'] = Usuario[5]
            Email_Encontrado = True
            return jsonify({'success': True, 'Email_Encontrado': Email_Encontrado})
        else:
            Email_Encontrado = False
            return jsonify({'success': True, 'Email_Encontrado': Email_Encontrado})
    except Exception as e:
        return jsonify({'success': False, 'Email_Encontrado': Email_Encontrado})



@app.route("/Novo_Cadastro", methods=['POST'])
def Novo_Cadastro():
    Novo_Usuario_Dados = request.get_json()
    Nome = Novo_Usuario_Dados.get('Nome_Completo')
    Email = Novo_Usuario_Dados.get('Email')
    Senha = Novo_Usuario_Dados.get('Senha')
    Confirmar_Senha = Novo_Usuario_Dados.get('Confirmar_Senha')
    Senha_Igual = False

    if Senha == Confirmar_Senha:
        Senha_Igual = True

        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Usuarios (Nome, Email, Senha) VALUES (%s, %s, %s)", (Nome, Email, Senha))
            mysql.connection.commit()
            cur.execute("SELECT u.UsuarioID, u.Nome, u.Email, u.Senha, u.DataCriacao, a.Caminho_Imagem FROM Usuarios u JOIN Avatar a ON u.AvatarID = a.AvatarID WHERE u.Email = %s;", (Email,))
            Usuario = cur.fetchone()
            cur.close()

            session['ID_Usuario_Logado'] = Usuario[0]
            session['Nome_Usuario_Logado'] = Usuario[1]
            session['Email_Usuario_Logado'] = Usuario[2]
            session['Data_Usuario_Logado'] = Usuario[4]
            session['Imagem_Usuario_Logado'] = Usuario[5]

            return jsonify({'success': True, 'Senha_Igual': Senha_Igual})
        except Exception as e:
            return jsonify({'success': False, 'Senha_Igual': Senha_Igual, 'error': str(e)})
    
    return jsonify({'success': True, 'Senha_Igual': Senha_Igual})


@app.route('/Desconectar', methods=['POST'])
def Desconectar():
    session.pop('ID_Usuario_Logado', None)
    session.pop('Nome_Usuario_Logado', None)
    session.pop('Email_Usuario_Logado', None)
    session.pop('Data_Usuario_Logado', None)
    session.pop('Imagem_Usuario_Logado', None)
    return jsonify({'success': True})

@app.route('/Trocar_Avatar', methods=['POST'])
def Trocar_Avatar():
    id = request.form.get('id')
    ID_Logado = session.get('ID_Usuario_Logado')
    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Usuarios SET AvatarID = %s WHERE UsuarioID = %s", (id, ID_Logado))
        mysql.connection.commit()
        cur.close()
        
        Email = session.get('Email_Usuario_Logado')
        cur = mysql.connection.cursor()
        cur.execute("SELECT u.UsuarioID, u.Nome, u.Email, u.Senha, u.DataCriacao, a.Caminho_Imagem FROM Usuarios u JOIN Avatar a ON u.AvatarID = a.AvatarID WHERE u.Email = %s;", (Email,))
        Usuario = cur.fetchone()
        cur.close()
        session['Imagem_Usuario_Logado'] = Usuario[5]
        
        return redirect(url_for('Configuracao_Usuario'))
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/Atualizar_Dados_Usuario' , methods=['POST'])
def Atualizar_Dados_Usuario():
    CEP = request.form.get('CEP')
    endereco = consultar_cep(CEP)
    Rua = endereco.get('logradouro')
    Bairro = endereco.get('bairro')
    Cidade = endereco.get('localidade')
    Estado = endereco.get('uf')
    Numero = request.form.get('Numero')
    if endereco:
         # Inserir novo endereço e atualizar o usuário
        cur = mysql.connection.cursor()
        try:
            cur.execute("SELECT EnderecoID FROM Usuarios WHERE UsuarioID = %s;", (session.get('ID_Usuario_Logado'),))

            EnderecoID = cur.fetchone()[0]
            if  EnderecoID == None:
                # Inserir novo endereço
                cur.execute("INSERT INTO EnderecoUsuario (Rua, Numero, Bairro, Cidade, Estado, CEP) VALUES (%s, %s, %s, %s, %s, %s)",
                            (Rua, Numero, Bairro, Cidade, Estado, CEP))

                # Recuperar o ID do novo endereço
                cur.execute("SELECT LAST_INSERT_ID()")
                novo_endereco_id = cur.fetchone()[0]

                # Atualizar o usuário com o ID do novo endereço
                cur.execute("UPDATE Usuarios SET EnderecoID = %s WHERE UsuarioID = %s", (novo_endereco_id, session.get('ID_Usuario_Logado')))

                # Confirmar a transação
                mysql.connection.commit()
            else:
                cur.execute("UPDATE EnderecoUsuario SET Rua = %s, Numero = %s, Bairro = %s, Cidade = %s, Estado = %s, CEP = %s WHERE EnderecoID = %s;",
                            (Rua, Numero, Bairro, Cidade, Estado, CEP, EnderecoID))
                mysql.connection.commit()
        except MySQLdb.Error as e:
            mysql.connection.rollback()
            print(f"Erro: {e}")
        finally:
            # Fechar cursor
            cur.close()
    else:
        print("CEP não encontrado.")
    return redirect(url_for('Configuracao_Usuario'))

@app.route('/Configuracao_Usuario')
def Configuracao_Usuario():
    Nome_Inteiro_Logado = session.get('Nome_Usuario_Logado')
    if session.get('Nome_Usuario_Logado'):
        Nome_Logado = session.get('Nome_Usuario_Logado').split()[0]
    else:
        Nome_Logado = None
    
    ID_Logado = session.get('ID_Usuario_Logado')
    Email_Logado = session.get ('Email_Usuario_Logado')
    Data_Logado = session.get ('Data_Usuario_Logado')
    Imagem_Usuario_Logado = session.get('Imagem_Usuario_Logado')


    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT eu.EnderecoID, eu.Rua, eu.Numero, eu.Bairro, eu.Cidade, eu.Estado, eu.CEP FROM Usuarios u JOIN EnderecoUsuario eu ON u.EnderecoID = eu.EnderecoID WHERE u.UsuarioID = %s;", (session.get('ID_Usuario_Logado'),))
        Usuario = cur.fetchone()
        cur.close()

        Cep_Logado = Usuario[6]
        Rua_Logado = Usuario[1]
        Bairro_Logado = Usuario[3]
        Cidade_Logado = Usuario[4]
        Estado_Logado = Usuario[5]
        Numero_Logado = Usuario[2]
        return render_template("Configuracao_Usuario.html",ID_Logado=ID_Logado, Nome_Inteiro_Logado = Nome_Inteiro_Logado,  Nome_Logado=Nome_Logado,  Email_Logado = Email_Logado, Data_Logado=Data_Logado,
                               Imagem_Usuario_Logado = Imagem_Usuario_Logado, Cep_Logado=Cep_Logado, Rua_Logado = Rua_Logado,
                                Bairro_Logado = Bairro_Logado, Cidade_Logado=Cidade_Logado, Estado_Logado = Estado_Logado, Numero_Logado = Numero_Logado)
    except Exception as e:
        return render_template("Configuracao_Usuario.html",ID_Logado=ID_Logado, Nome_Inteiro_Logado = Nome_Inteiro_Logado,  Nome_Logado=Nome_Logado,  Email_Logado = Email_Logado, Data_Logado=Data_Logado, Imagem_Usuario_Logado = Imagem_Usuario_Logado)


