import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  Gender = int(request.form['Gender'])
  Senior_Citizen = int(request.form['Senior_Citizen'])
  Phone_Service = int(request.form['Phone_Service'])
  Tech_Support = int(request.form['Tech_Support'])
  Streaming_Movies = int(request.form['Streaming_Movies'])
  Contract = int(request.form['Contract'])
  Payment_Method = int(request.form['Payment_Method'])
  predicao = model.predict(['Gender'])
  predicao = model.predict(['Senior_Citizen'])
  predicao = model.predict(['Phone_Service'])
  predicao = model.predict(['Tech_Support'])
  predicao = model.predict(['Streaming_Movies'])
  predicao = model.predict(['Contract'])
  predicao = model.predict(['Payment_Method'])
  return render_template('predicao.html', predicao=predicao[0])
  
  
app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)

# git add .

# git commit -m "nomenovo"
# git push

