# Repeat function

"""
Create a function that gives a greeting cyclically according to the names of 
a list
"""
list = ["Jennifer","Mary","Bruno"]
def saludar(nombre,pais):
    print(f"Hola {nombre} de {pais}")
for e in range(3):
    saludar(list[e],"Quebec")