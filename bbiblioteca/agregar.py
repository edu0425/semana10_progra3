# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:43:47 2022

@author: carlo
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")
# Recordemos que al insertar el ID es autoincrement
consulta=""" INSERT INTO
                PAIS(NOMBRE, ESTADO)
                VALUES('BRASIL', 'A')
         """
         
cursor = conexion.cursor()
cursor.execute(consulta)

# Nunca olviden hacer commit
conexion.commit()
conexion.close()