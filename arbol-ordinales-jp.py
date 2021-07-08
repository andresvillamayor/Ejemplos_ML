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
from sklearn import preprocessing


#lectura de datos 
data= pd.read_csv('creditos.csv',sep =',')

#verificacion de los datos 
print(data.head())

#validacion del dataframe 
print(pd.isnull(data).sum()) #tipo cartera tiene 3777 valores faltantes Nan

#calular los la edad  verificacion de datos

data['fechaHora'] = pd.to_datetime(data['fechaHora'])
data['nacimiento'] = pd.to_datetime(data['nacimiento'])
data['edad'] = ((data['fechaHora']-data['nacimiento'])/np.timedelta64(1,'Y')).astype(int)
#columna edad esta en el ultimo lugar del dataframe

# seleccionar variables y target, descartar variables pos aprobación
# utilizando Hold out 
df1 = data.iloc[:,2:3]
df2 = data.iloc[:,83:84]
df3 = data.iloc[:,4:68]
df4 = data.iloc[:,82:83]

# # Unificar en un dataframe filtrado
df = pd.concat([df1,df2,df3,df4], axis=1)
print (df.shape) # cantidad de filas y columnas
#verificar en el explorador de variables los cambios 
#Modificar los datos  LabelEncoder()
#Codificar cada variable categorica con su propio encoder sin utilizar el replace 
#Nacionalidad
var_nacionalidad = preprocessing.LabelEncoder()
df["nacionalidad"] = var_nacionalidad.fit_transform(df["nacionalidad"])
#Sexo (M,F)
var_sexo = preprocessing.LabelEncoder()
df["sexo"] = var_sexo.fit_transform(df["sexo"].astype(str))
#Estado Civil(S,C)
var_estcivil = preprocessing.LabelEncoder()
df["est_civil"] = var_estcivil.fit_transform(df["est_civil"].astype(str))
# Cargo que ocupa  (Empleado)
var_ocupcargo = preprocessing.LabelEncoder()
df["ocup_cargo"] = var_ocupcargo.fit_transform(df["ocup_cargo"].astype(str))
#Cliente Nuevo o Recurrente (N/R)
var_cliente = preprocessing.LabelEncoder()
df["cliente_nuevo_o_recurrente"] = var_cliente.fit_transform(df["cliente_nuevo_o_recurrente"])
#Ver si tiene tarjeta Visa Clasica 
var_tienevisa = preprocessing.LabelEncoder()
df["tiene_visa_classic"] = var_tienevisa.fit_transform(df["tiene_visa_classic"])
#ver si tiene visa Gold
var_tienevisagold= preprocessing.LabelEncoder()
df["tiene_visa_gold"] = var_tienevisagold.fit_transform(df["tiene_visa_gold"])
#tiene mastercard gold
var_mastercardgold = preprocessing.LabelEncoder()
df["tiene_mc_gold"] = var_mastercardgold.fit_transform(df["tiene_mc_gold"])
#tiene fc
var_tienefc = preprocessing.LabelEncoder()
df["tiene_fc"] = var_tienefc.fit_transform(df["tiene_fc"])
#tiene mastercard clasica
var_mastercardclasica = preprocessing.LabelEncoder()
df["tiene_mc_classic"] = var_mastercardclasica.fit_transform(df["tiene_mc_classic"])
#ver la Faja
var_faja = preprocessing.LabelEncoder()
df["respuesta_iconf_faja_score"] = var_faja.fit_transform(df["respuesta_iconf_faja_score"].astype(str))
#ver target Resultado final 
var_resultadofinal = preprocessing.LabelEncoder()
df["resultadoFinal"] = var_resultadofinal.fit_transform(df["resultadoFinal"])

########
# split dataset en train (70%) y test (30%)
X = df.iloc[:,0:66  ]
y = df['resultadoFinal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Entrenar decision tree usando entropia y profundidad maxima 6
clf = DecisionTreeClassifier(criterion="entropy",min_samples_leaf=50,max_depth=6)
clf = clf.fit(X_train,y_train)

# Predecir con datos de test
y_pred = clf.predict(X_test)
print('-----------------------------------------------------------------------------------------')
# Accuracy: (tp+tn)/n -  donde n es la cantidad de FP+FN+TP+TN
print("Accuracy - Acertividad y Ecxactitud de las muestras:",metrics.accuracy_score(y_test, y_pred))
print(metrics.precision_recall_fscore_support(y_test, y_pred, average=None))
print('-----------------------------------------------------------------------------------------')
print (
       'Se entreno el modelo con 30% de datos 0.3 en el test_size'
       ' usando entropia con max de profundiad de 6' 
       'Este modelo esta inclinado por hacia los creditos malos con un % 88 '
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
                special_characters=True, feature_names = X.columns,class_names = ['BIEN','MAL'])

(graph,) = pydot.graph_from_dot_file('creditos.dot')
graph.write_png('creditos.png')

