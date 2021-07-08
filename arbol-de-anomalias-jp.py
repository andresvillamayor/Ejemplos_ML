#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 19:56:55 2020
Profesor Julio Paciello
Insolation Forrest
Deteccion de anomalias Tecnica no supervisada   
@author: andyvillamayor
"""

# Importacion de Librerias

import pandas as pd 
from sklearn.ensemble import IsolationForest
from sklearn import metrics

# Leer csv con datos y cargar en el dataframe data 
data = pd.read_csv("creditcard.csv") 

# Preview de las 5 primeras filas de data, total filas: 284807
print (data.head(5))

# total confirmado como fraude (class=1): 492
data[data['Class']==1]


######### PREPARACION DE DATOS 

# train con % de registros con Class=0
# 50%(1)- 50% (-1) 
# 2 X 1 
#cantida de variables para  la preparacion de modelo 
####################################################
n = 2000   
X_train = (data[data["Class"]==0].iloc[0:n,0:30])
print(X_train)
print(X_train.info())


# test1 492 registros con Class=1, y_test1 colocamos -1 para poder comparar con score de clasificacion

# test0 500 registros con Class=0 (disjunto de train), y_test0 colocamos 0 para poder comparar con score de clasificacion

#conjunto de valores anomalos
#############################
X_test1 = data[data["Class"]==1].iloc[:,0:30] 
y_test1 = data[data["Class"]==1].iloc[:,30:31]
y_test1['Class']=-1
print('X_test 1')
print('--------')
print (X_test1)
print ('y_test1')
print('--------')
print(y_test1)

#conjunto de valores normales
#############################
X_test0 = data[data["Class"]==0].iloc[n:n+500,0:30]
y_test0 = data[data["Class"]==0].iloc[n:n+500,30:31]
y_test0['Class']=1

print('X_test0')
print('--------')
print (X_test0)
print ('y_test0')
print('--------')
print(y_test0)

# unificar TEST 
X_test = pd.concat([X_test1,X_test0], axis=0) # valores normales 500
y_test = pd.concat([y_test1,y_test0], axis=0) # concatena los dataframe

print('X_test')
print('--------')
print (X_test)
print ('y_test')
print('--------')
print(y_test)

# entrenamiento del modelo --->sklearn.isolationforest // en contaminacion 'auto' por defecto o valor 
# en python no acepta contamination ='0,1' ----> 0.1 en caso contrario dara un error en el X_train
clf = IsolationForest(behaviour='new', max_samples=1000, n_estimators=10,random_state=1, contamination=0.1)
clf.fit(X_train)
y_pred_test = clf.predict(X_test)


#juntamos los dataset con el zip 
dtest = pd.DataFrame(zip(y_test['Class'],y_pred_test), 
                  columns=['actual test','score pred test'])

dtest[dtest['score pred test']==-1]
print("Accuracy:",metrics.accuracy_score(dtest['actual test'], dtest['score pred test']))
print(metrics.precision_recall_fscore_support(dtest['actual test'], dtest['score pred test'], average=None))

print('Matriz de Confusion')
print('-------------------')
print(pd.crosstab(dtest['actual test'], dtest['score pred test'], 
            rownames=['actual'], 
            colnames=['pred'], margins=False, margins_name="Total"))
