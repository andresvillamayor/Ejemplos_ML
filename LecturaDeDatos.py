#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: andyvillamayor
"""
# -------------------------------------------------------
# Librerias a ser utilizadas
# -------------------------------------------------------
import pandas as pd
import numpy as np 
from CalculoDeDistancia import valorDimension
from CalculoDeDistanciaSimplices import CalcularSimplices
# --------------------------------------------------------    
# Archivo de Datos a ser procesados 
# Datos 
# --------------------------------------------------------
data_valor = pd.read_excel('Data.xls')

# Archivo con la definicion de datos
# Definiciones de tipo 
# Dimension-Tipo de Dato, Distancia Metrica - Peso 
# --------------------------------------------------------
data_def = pd.read_excel('Data-Def.xls')

# Data 
# variable donde guarda la dimension de la matriz de datos 
# --------------------------------------------------------
dimension_matriz_Data = []
for f in data_valor.shape:
     dimension_matriz_Data.append(f)

# creacion de listas     
dim_fila= (dimension_matriz_Data[0]) 
dim_columna = (dimension_matriz_Data[1]) 
# cantidad de fila en Data (numpy)
fila_data_valor = np.array(dim_fila) 
# cantidad de columans en Data (numpy)
columna_data_valor = np.array(dim_columna)
columna2_data_valor = (columna_data_valor -1)

# Data-Def
# Definiciones de de Data-Def  
#-------------------------------------------------------
# creacion de listas 
fila_dato = []  
fila_distancia =[] 
fila_peso=[] 
# volcado de los datos a los vectores
fila_dato = data_def.iloc[0]
fila_distancia = data_def.iloc[1]
fila_peso = data_def.iloc[2]
# volcado de listas a numpy
fila_dato_data_def = np.array(fila_dato)
fila_distancia_data_def = np.array(fila_distancia)
fila_peso_data_def = np.array(fila_peso)

# Funcion 
# --------------------------------------------------------
def matriz_distancia(m,vuelta,fila_data_valor):   
    print ('valos de Suma  de matriz :-------------------->', vuelta) 
    if vuelta == 0:
        global total
        total= np.zeros((fila_data_valor,fila_data_valor))
        total = total + m
    else:
        total = total + m     
    return   total  

# --------------------------------------------------------
# Inicio de lecutra de dimensiones del archivo Data
# --------------------------------------------------------
vuelta = 0
dataset = []
valor_resultado = []
lista = []
while vuelta <= columna2_data_valor:
    matriz_calculada = []
    print('lee dimension:',vuelta)
    data_valor_d = data_valor.iloc[:,vuelta]
    #carga los datos en el dataset 
    for d in data_valor_d:
        dataset.append(d)         
    matriz_dimension = ( valorDimension(vuelta,fila_data_valor,fila_dato[vuelta],fila_distancia[vuelta],fila_peso[vuelta],dataset))
    matriz_calculada = np.array(matriz_dimension).reshape(fila_data_valor,fila_data_valor)
    total = matriz_distancia(matriz_calculada,vuelta,fila_data_valor)
    
    if vuelta == 0:
       
          df_ma1 = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 1:
         
          df_ha1 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 2:
         
          df_ma2 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 3: 
          df_ha2 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 4: 
          df_eu1 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 5: 
          df_eu2 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 6: 
          df_eu3 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 7: 
          df_eu4 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 8: 
          df_eu5 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 9: 
          df_eu6 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 10: 
          df_eu7 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    elif vuelta == 11: 
          df_eu8 =  df_ma = pd.DataFrame(matriz_calculada)
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor)) 
    elif vuelta == 12: 
          df_eu9 =  df_ma = pd.DataFrame(matriz_calculada)    
          lista.append(np.array(matriz_calculada).reshape(fila_data_valor,fila_data_valor))
    df_dist = pd.DataFrame(total)

    vuelta = vuelta + 1
print(CalcularSimplices(lista))
# Lectura de simplices
print('fin de lectura')    
#df_dist.to_csv(r'distancia_total.csv', index = False, header=True)   



