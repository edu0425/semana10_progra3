# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:16:05 2022

@author: carlo
"""

try:
    numerador=float(input("Numerador: "))
    denominador=float(input("Denominador: "))
    resultado=numerador/denominador
    print(f"Resultado= {resultado}")
    print("Gracias")
    
except ZeroDivisionError:
    print("No puedes dividir entre CERO")
    
except:
    print("Hubo un ERROR")
    
else:
    print("La division se realizó correctamente")
finally:
    print("La operacion terminó!")