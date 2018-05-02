# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:46:37 2018

@author: RIVERA
"""

"""
*******************************************************************************
            USO DE TIPOS DE DATOS
*******************************************************************************
"""


#%%

"""
*******************************************************************************
                    CADENAS O STRINGS
*******************************************************************************
"""

cadena1 = "Primera cadena en phyton"
cadena2 = "Siempre poner en comillas"
print(cadena1)
print(cadena2)
print(cadena1, cadena2)
print(type(cadena1))

#%%

cadenaUnida = cadena1 + " " + cadena2
print(cadenaUnida)

#%%

nombre = "Kike"
ciudad = "La Paz"
presentacion = "Hola me llamo {}, y naci en {}".format(nombre, ciudad)
print(presentacion)


#%%

presentacion2 = f"Hola me llamo {nombre}, soy de {ciudad}"
print(presentacion2)

#%%

titulo = "mas operaciones CON STRINGS"
print(titulo.upper())
print(titulo.lower())
print(titulo.capitalize())

