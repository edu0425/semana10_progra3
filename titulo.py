# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:55:17 2022

@author: carlo
"""

# Problema: Necesitamos mostrar los nombres de una cadena 
# presentando las primeras letras enn mayuscula
# En word se conoce como formato Titulo


#importar libreria
import camelcase

nombre="carlos eduardo granados pretel"
print(nombre.upper())
print(nombre.title())


# Creamos un objeto llamado cam

cam=camelcase.CamelCase()
print("con camelcase.......")

#Imprimimos el nombre en formato titulo
#utilizamos el camelcase

print(cam.hump(nombre))

# Para resolver el siguiente problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluimos los argumentos
#   'carlos' y 'pretel'

cam2=camelcase.CamelCase('carlos', 'pretel')
print(cam2.hump(nombre))

