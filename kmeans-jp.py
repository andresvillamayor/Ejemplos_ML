#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 08:18:29 2020
Profesor Julio Paciello
Kmeans - No supervisado 
Segmentacion - Clustering 
@author: andyvillamayor
"""
#Librerias 
import pandas as pd 
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
from sklearn import preprocessing

# Leer csv con datos y cargar en el dataframe data
data = pd.read_csv("creditos.csv") 

# calcular variable edad a partir de fecha de solicitud - fecha de nacimiento
data['fechaHora'] = pd.to_datetime(data['fechaHora'])
data['nacimiento'] = pd.to_datetime(data['nacimiento'])
data['edad'] = ((data['fechaHora']-data['nacimiento'])/np.timedelta64(1,'Y')).astype(int)

print(data.head(5))

### PREPARACION DE DATOS 
## Seleccion de los datos que van a ser segmentados o clasterizados  
df = data[['edad','cliente_nuevo_o_recurrente','monto_solicitado','tiene_ips',
           'plazo_solicitado','ingreso_neto_mensual','resultadoFinal']]

print(df) 
# One-hot encoding para variables categoricas
x = pd.get_dummies(df)

# Normalizacion a [0-1]
min_max_scaler = preprocessing.MinMaxScaler()
xNorm = pd.DataFrame(min_max_scaler.fit_transform(x.values))
print(xNorm.head(5))
print(xNorm.shape) # filas y columnas

# Verificacion de la cantidad de cluster que voy a usar 

# Elbow Curve  ( Curva de Elbow)
nc = range(1, 25)
kmeans = [KMeans(n_clusters=i) for i in nc]
score = [kmeans[i].fit(xNorm).score(xNorm) for i in range(len(kmeans))]
    
plt.plot(nc, score, color='green') 
plt.xlabel('Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

# CLUSTERIZACION
kmeans = KMeans(n_clusters=8, max_iter=300, random_state=1)
kmeans.fit(xNorm)
print("Score: " + str(kmeans.score(xNorm)))
print(kmeans.labels_)
#print(kmeans.cluster_centers_)

clusters = pd.DataFrame(min_max_scaler.inverse_transform(kmeans.cluster_centers_), columns=x.columns)
clusters['tiene_ips'] = clusters['tiene_ips'].round()
clusters['cliente_nuevo_o_recurrente_N'] = clusters['cliente_nuevo_o_recurrente_N'].round()
clusters['cliente_nuevo_o_recurrente_R'] = clusters['cliente_nuevo_o_recurrente_R'].round()
clusters['resultadoFinal_BIEN'] = clusters['resultadoFinal_BIEN'].round()
clusters['resultadoFinal_MAL'] = clusters['resultadoFinal_MAL'].round()
clusters

xFinal = pd.concat([x,pd.DataFrame(list(kmeans.labels_),columns=['label'])],axis= 1)
print('Cluster 0', xFinal[xFinal['label']==0])
print('Cluster 1', xFinal[xFinal['label']==1])
print('Cluster 2',xFinal[xFinal['label']==2])
print('Cluster 3',xFinal[xFinal['label']==3])
print('Cluster 4',xFinal[xFinal['label']==4])
print('Cluster 5',xFinal[xFinal['label']==5])
print('Cluster 6',xFinal[xFinal['label']==6])
print('Cluster 7',xFinal[xFinal['label']==8])

