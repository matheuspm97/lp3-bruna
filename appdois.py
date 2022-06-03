from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("modelo.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("homepage.html")




@app.route("/predicao", methods = ["GET", "POST"])
@cross_origin()
def predicao():
    if request.method == "POST":

        # Date_of_Journey
        churn = request.form["churn"]
        predicao = int(pd.churn(churn, format="0, 1, 2, 3"))
        
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        naochurn = int(pd.churn(churn, format ="0"))
        
        # Arrival
        churn_arr = request.form["Predict_churn"]
        Arrival_churn = int(pd.to_churn(churn_arr, format ="0, 1, 2,3"))
       # print("Arrival : ", Arrival_hour, Arrival_min)

        # Total Stops
        Total_churn = int(request.form["Prediction_churn"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        churn=request.form['churn']
        if(churn=='Gender'):
            Gender = 0
            Masculino = 0
            Feminino = 1
            

        elif (churn=='Senior_Citizen'):
            Senior_Citizen = 0
            Sim = 1
            Não = 0
            

        elif (churn=='Informe os serviços'):
            Phone_Service = 0
            Tech_Support = 1
            Streaming_Movies = 2
             
            
        elif (churn=='Payment_Method'):
            Cheque_eletrônico = 0
            Cheque_Físico = 1
            Transferência_Bancária = 2
            Cartão_de_Crédito = 3
            
            
        elif (churn=='Contract'):
            Mês_a_mês = 2
            Um_ano = 1
            Dois_ano = 0
                        
        
        # Source
        # Banglore = 0 (not in column)
        churn = request.form["Gender"]
        if (churn == 'Gender'):
            Masculino = 0
            Feminino = 1
           

        elif (churn  == 'Senior_Citizen'):
            Sim = 1
            Não = 0

        elif (churn  == 'Informe os serviços'):
            Phone_Service = 0
            Tech_Support = 1
            Streaming_Movies = 2

        elif (churn  == 'Payment_Method'):
            Cheque_eletrônico = 0
            Cheque_Físico = 1
            Transferência_Bancária = 2
            Cartão_de_Crédito = 3

        elif (churn  == 'Contract'):
            Mês_a_mês = 2
            Um_ano = 1
            Dois_ano = 0

        

             
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        prediction=model.predict([[
            Gender,
            Senior_Citizen,
            Phone_Service,
            Tech_Support,
            Streaming_Movies,
            Contract,
            Payment_Method,
            
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Cliente. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)