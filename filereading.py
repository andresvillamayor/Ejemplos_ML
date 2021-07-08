#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: andyvillamayor
"""

""" Commentary
This program is to read columns from a file and pass a function to return
a distance matrix.
"""
#  Libraries
#  ---------

import pandas as pd
import numpy as np
from calculatedistance import calcular_matriz



def leer_archivo_data():
    'Read the files from the file directory.'
    
    try:
        data_valor = pd.read_excel('./input_file/Data.xls')
        return data_valor
    except:
        print ('ERROR in FILE INPUT - DATA')
   
     


def dimension_archivo_data(data_valor):
    'Load dimension for data_valor.'
    dimension_matriz_data_valor = []
    for a in data_valor.shape:
        dimension_matriz_data_valor.append(a)

    return dimension_matriz_data_valor


def leer_archivo_definicion():
    'File data definition.'
    try:
        data_def = pd.read_excel('./input_file/Data-Def.xls')
        return data_def
    except:
        print('ERROR in FILE INPUT- DATA FILE')


def crear_matriz(matriz_distancia,fila_data_valor):
    total_distancia = np.asarray(matriz_distancia) 
    matriz = total_distancia.reshape(fila_data_valor,fila_data_valor)
    print ('Total Matriz :', (total_distancia).reshape(fila_data_valor,fila_data_valor))
    return matriz                                             

def crear_archivo(matriz):
    df_dist = pd.DataFrame(matriz)
    df_dist.to_csv(r'./output_file/distancia_total.csv', index = False, header=False)
    #df_dist.to_excel(r'./output_file/distancia_total.xlsx', index = False, header=False)
    return

def main():
    print('*****************************************************************')
    print( 'Starting the distance calculation program.')
    print('*****************************************************************')
    
    'Variable.'
    'List of data types.'
    # fila_dato = []
    # 'List of types of distance.'
    # fila_distancia = []
    # 'List of weights by variable.'
    # fila_peso = []
    # 'Data set by dimension or column.'
    
    
    'Run function to read file.'
    '--------------------------'
    data_valor = leer_archivo_data()
    dimension_data_valor = dimension_archivo_data(data_valor)
    'Number of rows or dimensions.'
    total_fila = dimension_data_valor[0]
    fila_data_valor = np.array(total_fila) 
    'Number of columns or dimensions.'
    total_columna = dimension_data_valor[1]
    columna_data_valor = np.array(total_columna)
    
    'Run function to read file definition.'
    '-------------------------------------'
    data_def = leer_archivo_definicion()
    'Data type row.'
    fila_dato = data_def.iloc[0]
    'Distance type row.'
    fila_distancia = data_def.iloc[1]
    valor_distancia = np.array(fila_distancia)
    'Weight row.'
    fila_peso = data_def.iloc[2]
                   
    #  ----------------------------------
    
    'Pass the parameters to the calculation function.'
    #print (datos_de_fila)
    matriz_distancia = []
    suma_distancia = []
    
    matriz_suma_distancia = np.array([])
    'Generate the data set.'
    data = data_valor.to_numpy()
    'Send the parameters to the function.'
    matriz_distancia= (calcular_matriz(data,columna_data_valor,fila_data_valor,valor_distancia))
    matriz = crear_matriz(matriz_distancia, fila_data_valor)
    crear_archivo(matriz)
    #print ('valor suma de distancia=', suma_distancia)
    #matriz_suma_distancia = matriz_distancia
    #print((matriz_distancia).reshape(fila_data_valor * fila_data_valor))
    #print(matriz_suma_distancia) 
    #crear_archivo(matriz_suma_distancia)
    print('*****************************************************************')    
    print('End of distance calculation see the generated file in output_file.')    
    print('*****************************************************************')

main()  