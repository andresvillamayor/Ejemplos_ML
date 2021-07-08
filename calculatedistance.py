#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@autor andy villamayor
"""

"""Commentary
Calculate the distances of the received datasets 
(calculation of different types of distances 
depending on the received parameter).
"""
#  Libraries
#  ---------
from scipy.spatial.distance import cityblock 
from scipy.spatial.distance import euclidean 
from scipy.spatial.distance import hamming
from scipy.spatial.distance import chebyshev
import math
import numpy as np

"""
The distance functions receive 4 parameters, point 1, point2, 
data type and the weight, they are defined in the data definition file.
"""
#  Functions
#  ---------
def validar_positivo_entero(p):
    'Verify that the value is positive.'
    valor = ''       
    dato = p
      
    if dato == '':
        valor = 'Neutro'
    elif dato < int(0):
        valor ='Negativo'
    else:
        valor = 'Positivo'
    
    return valor 

def validar_positivo_flotante(p):
    valor= ''
    dato = p
    
    if dato == '':
        valor = 'Neutro'
    elif dato < float(0):
        valor ='Negativo'
    else:
        valor = 'Positivo'
    
    return valor

def calcular_tipo_dato(p,d):
    'Calculate the product between distance and weight.'
              
    'Check the data type.'    
            
    if (d == 'CA'):
        valor = (validar_positivo_entero(p))
        if (valor == 'Negativo'):  
            print ('Data Type Error.')
        elif (valor == 'Neutro'):
            p = 1
            return float(p)   
        else:
             return float(p)

    elif d =='DI':
        valor = (validar_positivo_entero(p))
        if (valor == 'Negativo'):
            print ('Data Type Error.')
        elif (valor == 'Neutro'):
            p = 1
            return float(p)
        else: 
            return float(p)
        
        

    elif d =='CO':
        valor = (validar_positivo_flotante(p))
        if valor =='Negativo':
            print ('Data Type Error.')
        elif (valor == 'Neutro'):
            p = 1
            return float(p)            
        else:
             return float(p)
          
        
def distance_ma(p1,p2):
    'Manhattan distance.'  
    dist = cityblock(p1,p2) 
    return dist 


def distance_ha(p1,p2):
    'Hamming distance.' 
    dist= hamming(p1, p2)  
    return dist


def distance_eu(p1,p2):
     'Eucledian distance.'
     dist = euclidean(p1,p2)
     return dist 

def distance_ch(p1,p2):
     'Chebyshev distance.' 
     dist = chebyshev(p1,p2)    
     return dist

def crear_matriz(valor_suma_distancia,fila,columna):
     m = np.valor.suma_distancia.reshape(fila,columna)      
     return m


def calculo(vector,p1,p2):
    'distance for D'
    valor_distancia = []
    valor =  0
    #print (p1)
    #print (p2)
    while valor < len(vector):
        if vector[valor] == 'HA':
           valor_distancia.append(distance_ha(p1[valor],p2[valor]))     
        elif vector[valor]== 'EU':
           valor_distancia.append(distance_eu(p1[valor],p2[valor]))      
        elif vector[valor] =='MA':
           valor_distancia.append(distance_ma(p1[valor],p2[valor]))
        else:
            None
        valor = valor + 1
        #print ('valor distancia entre los puntos es igual a =',np.sum(valor_distancia))
     #return np.sum(valor_distancia)
    return np.sum (valor_distancia)

def calcular_matriz(data,columna,fila,valor_distancia):

    'Sent parameters are received.'   
    valor_suma_distancia = [] 
    cuenta = 0
    while cuenta <= fila -1:
        print('Reading row -------->', cuenta )
        fila_uno = data[cuenta]
        #contador = cuenta
        contador = 0 
        while contador <= fila - 1:
            fila_dos = data[contador]     
            valor_dist =  calculo(valor_distancia,fila_uno,fila_dos)
            #print ('valor de distancia',valor_dist)
            valor_suma_distancia.append(valor_dist)
            #print ('total de distancia :', valor_suma_distancia)
            #print('distancia del array:',valor_suma_distancia)     
            #crear_matriz(valor_suma_distancia,fila,columna)
            #print (crear_matriz)
            #crear_matriz(suma_distancia, fila, columna)
            
            #  Crear matriz 
            
            contador = contador + 1
                      
        cuenta = cuenta + 1
        
    return valor_suma_distancia