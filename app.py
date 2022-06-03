from flask import Flask, render_template, jsonify, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Contatos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR NOT NULL, telefone VARCHAR NOT NULL)""")
    conn.close()

@app.route('/')
def homepage():
    # contatos = SELECT ...
    # abre conexão, executa SQL, fecha conexão
    conn = sqlite3.connect('homepage.html')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Contatos """)
    homepage = cursor.fetchall()        
    return render_template("index.html", homepage=homepage, quantidade=len(homepage))
    conn.close()


@app.route('/predicao', methods=['POST'])
def predicao():
    # novo_contato = {'nome': nome, 'telefone': telefone}
    # contatos.append(novo_contato) # INSERT INTO contatos VALUES (...)
    # abre conexão, executa SQL insert, fecha conexão
    conn = sqlite3.connect('predicao.html')
    cursor = conn.cursor()
    predicao.execute("predicao.html", predicao=predicao, quantidade=len(predicao))
    conn.commit()

    return redirect("/predicao.html")

if __name__ == '__main__':
    create_database()
    app.run(debug=True)



# import cloudpickle
# from flask import Flask, render_template, request
# import numpy as np
# #import Model

# import sklearn
# #from cloudpickle import svm
# from sklearn import datasets


# with open('model.pkl', 'rb') as file_in:
#   model = cloudpickle.load(file_in)

# app = Flask(__name__)

# @app.route('/')
# def homepage():
#   return render_template("homepage.html")

# @app.route('/predicao', methods=['POST'])
# def predicao():
#     # int_features=[int(x) for x in request.form.values()]
#     # Gender = request.form['Gender']
#     # Senior_Citizen = request.form['Senior_Citizen']
#     # Phone_Service = request.form['Phone_Service']
#     # Tech_Support = request.form['Tech_Support']
#     # Streaming_Movies = request.form['Streaming_Movies']
#     # Contract = request.form['Contract']
#     # Payment_Method = request.form['Payment_Method']
#     # predicao = model.predict([Gender],[Senior_Citizen],[Phone_Service],[Tech_Support],[Streaming_Movies], [Contract],[Payment_Method])
#     return render_template("predicao.html", predicao=predicao)

# #if serve para dizer que esse site sera executa quando eu executar esse código diretamente(botão direito, executar), agora se for importado de outro arquivo eu não executo o que esta aqui dentro.
# if __name__ == "__main__":
#   app.run(debug=True)


# #servidor do heroku



