# Operador ternario
"""
Elaborar un programa que pida al usuario 
un numero y si es par lo eleve al cubo, 
y si no es par lo eleve al cuadrado
"""

numero = input("Ingrese un numero:")

try:
    numero = float(numero)
except:
    print("Ingrese un numero valido")
    exit()
elevado = numero**3 if (numero%2)==0 else numero**2

print(f"Su resultado es: {elevado}")