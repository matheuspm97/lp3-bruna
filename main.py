#importa biblioteca
import pandas as pd 
import numpy as np

#importa dados
dataframe = pd.read_csv('/content/train.csv', sep=',')

#traz a quantidade de linhas e colunas
dataframe.shape

dataframe['Contract'].unique()

#mostra as 5 primeiras linhas
dataframe.head()

"""## Análise Exploratória"""

#Trazer informação das colunas
dataframe.info()

#traz informações como contagem, media, minimo,  1/4 1/2 3/4 maximo
dataframe.describe()

#Histograma dos atributos numericos
dataframe.hist(bins=50, figsize=(20,15))

#Coeficiente de correlação
dataframe.corr()

"""## Limpeza dos dados"""

#Somar nulos
dataframe.isnull().sum()

#substituir espaço por "_"
dataframe.columns = dataframe.columns.str.replace(' ', '_')

#Limpeza de nulos


df=dataframe

df.dropna(subset=['Total_Charges' ], inplace=True)

#Converter texto em binario
df['Gender'] = np.where(df.Gender	 == 'Yes',1,0)
df['Senior_Citizen'] = np.where(df.Senior_Citizen	 == 'Yes',1,0)
df['Partner'] = np.where(df.Partner == 'Yes',1,0)
df['Phone_Service'] = np.where(df.Phone_Service == 'No phone service',0,
                      np.where(df.Phone_Service == 'No',1,2))

df['Internet_Service'] = np.where(df.Internet_Service == 'DSL',0,
                      np.where(df.Internet_Service == 'Fiber optic',1,2))  


df['Churn'] = np.where(df.Churn == 'Yes',1,0)


df['Dependents'] = np.where(df.Dependents == 'Yes',1,0)

df['Multiple_Lines'] = np.where(df.Multiple_Lines == 'Yes',1,0)
df['Online_Security'] = np.where(df.Online_Security == 'Yes',1,0)
df['Device_Protection'] = np.where(df.Device_Protection == 'Yes',1,0)
df['Tech_Support'] = np.where(df.Tech_Support == 'Yes',1,0)


df['Tenure'] = np.where(df.Tenure	 == 'Yes',1,0)

df['Online_Backup'] = np.where(df.Online_Backup	 == 'Yes',1,0)


df['Streaming_Movies'] = np.where(df.Streaming_Movies == 'Yes',1,0)
df['Contract'] = np.where(df.Contract == 'Yes',1,0)
df['Paperless_Billing'] = np.where(df.Paperless_Billing == 'Yes',1,0)




df['Payment_Method'] = np.where(df.Payment_Method == 'Electronic check',0,
                      np.where(df.Payment_Method == 'Mailed check',1,
                      np.where(df.Payment_Method == 'Bank transfer (automatic)',2,        
                     np.where(df.Payment_Method ==  'Credit card (automatic)',3,4))))  
      

#Converter para numero inteiro
df['Monthly_Charges'] = df['Monthly_Charges'].astype(np.int64)
df['Total_Charges'] = df['Total_Charges'].astype(np.int64)

"""## Extração de características"""

#definição das caracteristicas
X=df.drop(columns=['CustomerID','Partner','Dependents','Churn','Tenure','Multiple_Lines','Online_Security','Churn','Online_Backup','Device_Protection','Paperless_Billing','Monthly_Charges','Total_Charges', 'Internet_Service','Streaming_TV'])
y = df['Churn']

#Trazer informação das colunas
X.info()
X.head()

"""## Treinamento do modelo"""

#dividu a base de teste em 20% dos dados
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#utilizamos o algoritmo de floresta randomica
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=200, random_state=0) 
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)

classificador = RandomForestClassifier(class_weight='balanced')

classificador.fit(X_train, y_train)

"""## Avaliação do modelo"""

resultado = classificador.predict(X_test)

resultado

from sklearn import metrics

print(metrics.classification_report(y_test, resultado))

from sklearn.metrics import confusion_matrix

#matriz de confusão
confusion_matrix(y_test, resultado)

tn, fp, fn, tp = confusion_matrix(y_test, resultado).ravel()
print(tn, fp, fn, tp)

#acuracia
acuracia = (tp + tn)/ (tp + tn + fp + fn)
print(round(acuracia, 2))

import pickle

# save the model to disk
filename = 'model.pkl'
model=RandomForestClassifier()
pickle.dump(model, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
#loaded_model = pickle.load(open(model.pkl, 'rb'))
#result = loaded_model.score(X_test, y_test)
#print(result)