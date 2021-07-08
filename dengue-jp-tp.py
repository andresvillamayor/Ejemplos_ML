#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:20:00 2020
Redes Neuronales
@author: andyvillamayor
"""

#librerias
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt 

#leer datos csv
data= pd.read_csv('dengue_clima.csv', sep=',')
#verifico si no existe valores nulos dentro de las DataFrame
print(pd.isnull(data).sum())
#vemos la cabezera de datos del archivo 
print(data.head()) 
#vemos los datos de la correlacion entre las variables 
print(data.corr())

# Calculamos la correlacion positiva - negativa  (ambas sirven)
# pasamos el valor de datos de dataframe al de correlacion
data_corr = data.corr() 
##  filtra los datos con correlaciones mayores a 0.30 y menor a 1
##  filtra los Nan
data_corr[(abs(data_corr > 0.30)) & (data_corr < 1)]['cantidad'].dropna() 

print(data_corr)

## PREPARACION DE DATOS 
### Utilizamos PCA quitando las variables (cantidad -1) a (-11) variables lageadas 
### para evitar un autoregressive model

#generando dataframe para las variables ( 328 registros de muestras)

df1= data.iloc[:,11:99] # NO toma las variables lageadas cantidad
df2= data.iloc[:,100:] # se toma todas las variables a partir de 100 hacia arriba ( columnas)
df3= data.iloc[:,99:100] # se toma la variable target
#concatenacion de los dataframe 
df= pd.concat([df1,df2,df3],axis=1)   
# Validacion de datos en 
print('valores nulos')
print(pd.isnull(df).sum())

#276 registros para entrenamiento, 52 para validacion (52 semanas equivalente a 1 año)
#última columna es el target, todas las previas son input
#impresion de las cabeceras de las columnas
print (df.keys())

col = df.shape[1]
total = df.shape[0]
n = 276 # cantidad de registros para entrenamiento 
x = df.iloc[0:n,0:col-1]
x_val = df.iloc[n:,0:col-1]
y = df.iloc[0:n,col-1:col]
y_val = df.iloc[n:,col-1:col]

######## PCA 
#Crear PCA que explica el 98% de varianza acumulada
pca = PCA(n_components=0.90, svd_solver='full')
x = pca.fit_transform(x)
x_val = pca.transform(x_val)

#Entrenar el modelo y calcular predicciones
#MODELO MLP REGRESION 
modelo = MLPRegressor(hidden_layer_sizes=(50), max_iter=200,
                   activation='relu', solver='lbfgs', random_state=1)

modelo.fit(x, y['cantidad'])
y_pred = modelo.predict(x_val)
y_pred[y_pred < 0] = 0  # La NN puede lanzar valores negativos, normalizar a 0 esos casos

#graficar lo real y la prediccion 
semanas = range(total-n)
plt.plot(semanas, y_val, color='green') # REAL
plt.plot(semanas, y_pred, color='red') # PREDICCION
plt.show()
print('---------------------------------------------------------------------------------------')
# calcular coeficiente r2 y pearson
print("Coeficiente r2: " + str(modelo.score(x, y)))
print("Coeficiente de Pearson (r): " + str(sqrt(modelo.score(x, y))))
print('SE MANTIENE UNA ALTA CORRELACION , DEBIDO AL QUE EL PCA ESTA MUY CERCA DEL 100') 
print('SE VERA UNA MENOR CORRELACION CUANDO EL PCA ESTE MAS ALEJADO DEL 100')
print('---------------------------------------------------------------------------------------')

# calcular root mean square error (RMSE)
print('---------------------------------------------------------------------------------------')
print()
print("Raíz del Error cuadrático Medio (RMSE): " + str(sqrt(mean_squared_error(y_val, y_pred))))
print('---------------------------------------------------------------------------------------')
print("Media de Cantidad: " + str(y_val['cantidad'].mean()))
print('---------------------------------------------------------------------------------------')
print("% de error: " + str(sqrt(mean_squared_error(y_val, y_pred)) / y_val['cantidad'].mean()))
print('---------------------------------------------------------------------------------------')
print()
print('---------------------------------------------------------------------------------------')
print('PARA BAJAR EL ERROR SE BAJO EL PORCENTAJE DEL PCA A 90 , SE USO 3 NODOS EN LA CAPA OCULTA')
print('EL MAXIMO DE ITERACION DE 20 , LA ACTIVACION SE MODIFICO A LOGISTIC SIN BUEN RESULTADO') 
print('SE VOLVIO AL RELU DANDO MENOR ERROR PERO CON UN CORRELACION BUENA 60% ')
print('SE MODIFICO NUEMAVEMENTE LOS HIPERPARAMETROS PARA TENER UNA MEJOR VISION EN LA GRAFICA ')
print('FINALMENTE OTPO POR 50 NODOS OCULTOS Y 2OO ITERACIONES INTREMENTEANDO LA CORRELACION AL 99%')
print('SE MANTUVO EL PCA EN  90% ')
print('---------------------------------------------------------------------------------------')
#####################################################################################################

# Seleccion basada en correlacion de datos 
# Evitar autoregressive model para buscar variables independientes a la cantidad que puedan influir en ella
 
df2= data[[ 'temperatura_media_media(-7)','temperatura_media_media(-8)','temperatura_media_media(-9)',
              'temperatura_media_media(-10)','temperatura_media_media(-11)','nivel(-5)','nivel(-6)',
              'nivel(-7)','nivel(-8)','nivel(-9)','nivel(-10)','nivel(-11)','cantidad']]

# 276 registros para train, 52 para validacion (52 semanas equivalente a 1 año)
# última columna es el target, todas las previas son input
col = df2.shape[1]
total = df2.shape[0]
n = 276 # cantidad de muestras de pruebas 
x = df2.iloc[0:n,0:col-1]
x_val = df2.iloc[n:,0:col-1]
y = df2.iloc[0:n,col-1:col]
y_val = df2.iloc[n:,col-1:col]

#Entrenar el modelo y calcular predicciones
#MODELO MLP REGRESION 
modelo2 = MLPRegressor(hidden_layer_sizes=(100), max_iter=250,
                   activation='relu', solver='lbfgs', random_state=1)

modelo2.fit(x, y['cantidad'])
y_pred = modelo2.predict(x_val)
y_pred[y_pred < 0] = 0 # La NN puede lanzar valores negativos, normalizar a 0 esos casos

# graficar serie real y predicción
semanas = range(total-n)
plt.plot(semanas, y_val, color='green') # REAL
plt.plot(semanas, y_pred, color='red') # PREDICCION
plt.show()
print('---------------------------------------------------------------------------------------')

# calcular coeficiente r2 y pearson
print('---------------------------------------------------------------------------------------')
print("Coeficiente r2: " + str(modelo2.score(x, y)))
print('---------------------------------------------------------------------------------------')
print("Coeficiente de Pearson (r): " + str(sqrt(modelo2.score(x, y))))
print('---------------------------------------------------------------------------------------')
# calcular root mean square error (RMSE)
print('---------------------------------------------------------------------------------------')
print("Raíz del Error cuadrático Medio (RMSE): " + str(sqrt(mean_squared_error(y_val, y_pred))))
print('---------------------------------------------------------------------------------------')
print("Media de Cantidad: " + str(y_val['cantidad'].mean()))
print('---------------------------------------------------------------------------------------')
print("% de error: " + str(sqrt(mean_squared_error(y_val, y_pred)) / y_val['cantidad'].mean()))
print('---------------------------------------------------------------------------------------')

print('SE VOLVIO AL RELU DANDO MENOR ERROR PERO CON UN CORRELACION BUENA 60% ')
print('SE MODIFICO NUEMAVEMENTE LOS HIPERPARAMETROS PARA TENER UNA MEJOR VISION EN LA GRAFICA ')
print('FINALMENTE OTPO POR 100 NODOS OCULTOS Y 250 ITERACIONES INTREMENTEANDO LA CORRELACION ')
print(' ')