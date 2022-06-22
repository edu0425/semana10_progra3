# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:17:43 2022

@author: carlo
"""

# Importamos librerias basicas para leer archivos cvs

import csv

# Abrimos el archivo indicando el path y el encoding-utf para leer los cararcteres especiales

with open('Global_Mobility_Report.csv', encoding="utf8") as f:
    datos = csv.reader(f, delimiter=',')
    for fila in datos:
            print(f"{fila[0]}\t{fila[1]}\t{fila[2]}\t{fila[3]}\t{fila[4]}\t{fila[5]}\t{fila[6]}\t{fila[7]}\t{fila[8]}\t{fila[9]}\t{fila[10]}")