#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 9 09:23:19 2020
Arbol de Desiciones
@author: andyvillamayor
"""
#El calulo del arbol esta hecho automaticamente por DecisionTreeClassifier
#Parametros = entropia  valor maximo de desglose = 6 
#librerias 
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
import pydot


#lectura de datos 
data= pd.read_csv('creditos.csv',sep =',')

#verificacion de los datos 
print(data.head())

#validacion del dataframe 
print(pd.isnull(data).sum()) #tipo cartera tiene 3777 valores faltantes Nan

#calular los la edad 

data['fechaHora'] = pd.to_datetime(data['fechaHora'])
data['nacimiento'] = pd.to_datetime(data['nacimiento'])
data['edad'] = ((data['fechaHora']-data['nacimiento'])/np.timedelta64(1,'Y')).astype(int)
#columna edad esta en el ultimo lugar del dataframe
#verificar en el explorador de variables los cambios 


# seleccionar variables de la solicitud, sistema financiero y target, descartar variables pos aprobación
# utilizando Hold out 
df1 = data.iloc[:,2:3]
df2 = data.iloc[:,83:84]
df3 = data.iloc[:,4:68]
df4 = data.iloc[:,82:83]

# # Unificar en un dataframe filtrado
df = pd.concat([df1,df2,df3,df4], axis=1)

# One-hot encoding para variables categoricas
dfOHEncoded = pd.get_dummies(df)
dfOHEncoded.head()
# coloca de forma automatica modifica las variables cualitativas o categoricas a cuantitativas

# split dataset en train (70%) y test (30%)
X = dfOHEncoded.iloc[:,0:110]
y = dfOHEncoded['resultadoFinal_BIEN']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Entrenar decision tree usando entropia y profundidad maxima 6
clf = DecisionTreeClassifier(criterion="entropy",max_depth=4)
clf = clf.fit(X_train,y_train)

# Predecir con datos de test
y_pred = clf.predict(X_test)
print('-----------------------------------------------------------------------------------------')
# Accuracy: (tp+tn)/n -  donde n es la cantidad de FP+FN+TP+TN
print("Accuracy - Acertividad y Ecxactitud de las muestras:",metrics.accuracy_score(y_test, y_pred))
print(metrics.precision_recall_fscore_support(y_test, y_pred, average=None))
print('-----------------------------------------------------------------------------------------')
print (
       'Se entreno el modelo con 20% de datos 0.2 en el test_size'
       ' usando entropia con max de profundiad de 4'
       ' ,con una media de 0.88 % ( entre presicion y recall)'
       )
print('----------------------------')
print('Calcular matriz de confusion')
print('----------------------------')
#metrics.confusion_matrix(y_test, y_pred)
print(pd.crosstab(y_test, y_pred, 
            rownames=['actual'], 
            colnames=['pred'], margins=False, margins_name="Total")
)

# Obtener importancia de variables y vertificar variables mas relevantes
print('----------------------------')
print('Importancia de Variables')
print('Variables mas relevantes')
print('----------------------------')
fi = pd.DataFrame(zip(X.columns,clf.feature_importances_), columns=['feature','importance'])
print(fi[fi['importance'] > 0.0].sort_values(by=['importance'], ascending=False))



# cargar exportador de grafos y funcion de llamada a sistema
export_graphviz(clf, out_file="creditos.dot",  
                filled=True, rounded=True,
                special_characters=True, feature_names = X.columns,class_names = ['0','1'])

(graph,) = pydot.graph_from_dot_file('creditos.dot')
graph.write_png('creditos.png')
