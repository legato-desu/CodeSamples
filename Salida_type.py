# tipo de salidas
"""
Crea un programa que enseñe por pantalla el tipo de 
valor almacenado en la variable
"""
numero_1 = input("Ingrese un numero entero: ")
try:
    numero_1 = int(numero_1)
except:
    print("Ingrese un entero")
    exit()
numero_2 = input("Ingrese un numero flotante: ")    
try:
    numero_2 = float(numero_2)
except:
    print("Ingrese un flotante")

print(type(numero_1),type(numero_2))