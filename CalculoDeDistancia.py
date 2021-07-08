#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: andyvillamayor
"""
# Librerias a ser utilizadas
# ------------------------------------------------------
#import numpy as np
from scipy.spatial.distance import cityblock #Manhattan
from scipy.spatial.distance import euclidean #Euclediana
from scipy.spatial.distance import hamming   #Hamming

# Funciones de Distancias Metricas 
# --------------------------------

total_matriz = []
total= []
 

# distancia Manhattan    
def distanciaMA(p1,p2,p):
    dist = cityblock(p1,p2)
    if p == 0:
        p = 1
    else: None
    dist = dist * p 
    return dist 
# distancia Hamming
def distanciaHA(p1,p2,p):
    dist= hamming(p1, p2) 
    if p == 0:
        p = 1
    else: None
    dist = dist * p 
    return dist

# distancia Euclidea
def distanciaEU(p1,p2,p):
     dist = euclidean(p1,p2)
     if p == 0:
        p = 1
     else: None
     dist = dist * p 
     return dist 

#  

# para agregar en un vector las distancias 
def calcularMatrizDistancia(d):
    total_matriz.append(d)
    
    return total_matriz


def valorDimension(dimension,fila,dato,distancia,peso,dataset):
    distancia_metrica = []
    d = []
    if distancia == 'MA': # distancia Manhattan
         #calcularDimension(distancia,fila,peso,dataset)
         cuenta = 0
         while  cuenta <= fila:
              print('cuenta- vuelta:',cuenta,distancia)
              contador = 0
              
              while contador <= fila:
                  
                  distancia_metrica.append(distanciaMA(dataset[cuenta],dataset[contador],peso))
                  contador = contador + 1
                  
              cuenta = cuenta + 1 
        
         d = distancia_metrica    
            
    elif distancia == 'EU':
         cuenta = 0
         while  cuenta <= (fila)-1:
              print('cuenta- vuelta:',cuenta,distancia)
              contador = 0
              
              while contador <= (fila)-1:
                  distancia_metrica.append(distanciaEU(dataset[cuenta],dataset[contador],peso))  
                  
                  contador = contador + 1
                  
              cuenta = cuenta + 1 
                          
         d= distancia_metrica 
     
    elif distancia == 'HA':
         cuenta = 0
         while  cuenta <= (fila)-1:
              print('cuenta- vuelta:',cuenta,distancia)
              contador = 0
              
              while contador <= (fila)-1:
                  distancia_metrica.append(distanciaHA(dataset[cuenta],dataset[contador],peso))  
                  
                  contador = contador + 1
                  
              cuenta = cuenta + 1 
        
         d = distancia_metrica
                 
               
    return d
