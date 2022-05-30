import cloudpickle
from flask import Flask, render_template, request
import numpy as np
#import Model

import sklearn
from sklearn import svm
from sklearn import datasets

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template("homepage.html")

@app.route('/predicao', methods=['POST'])
def predicao():

  #predicao = '1'
  #lista = []

  #if predicao == 1:
  #print ('Churn')

  #if predicao <= 1:
  #print ('Não Churn') 

    int_features=[int(x) for x in request.form.values()]
    genero = request.form['genero']
    Senior_Citizen = request.form['Senior_Citizen']
    telefone= request.form['telefone']
    suporte= request.form['suporte']
    streaming= request.form['streaming']
    predicao = model.predict([genero],[idade],[telefone],[suporte],[streaming])
    return render_template("predicao.html", predicao=predicao)

#if serve para dizer que esse site sera executa quando eu executar esse código diretamente(botão direito, executar), agora se for importado de outro arquivo eu não executo o que esta aqui dentro.
if __name__ == "__main__":
  app.run(debug=True)


#servidor do heroku



