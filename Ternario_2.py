# Mayor de edad
"""
Elabore un programa que pida a dos 
usuarios el nombre y la edad e 
imprima el nombre del mayor
"""

nombre_1 = input("Ingrese el nombre del primer usuario: ")
edad_1 = input("Ingrese la edad del primer usuario: ")

try:
    edad_1 = int(edad_1)
except:
    print("edad no valida")    
    exit()
nombre_2 = input("Ingrese el nombre del segundo usuario: ")
edad_2 = input("Ingrese la edad del segundo usuario: ")

try:
    edad_2 = int(edad_2)
except:
    print("edad no valida")    
    exit()    
print(f"{nombre_1} es mayor ")if edad_1 > edad_2 else print(f"{nombre_2} es mayor")