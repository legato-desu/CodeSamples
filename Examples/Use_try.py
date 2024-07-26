# Use try

"""
Create a program that uses (try) to check a person's age 
and know if he is of legal age
"""
age = input("Ingrese su edad: ")
try:
    age = int(age)
except:
    print("Ingrese una edad valida") 
    exit()

if age >= 18:
    print("Eres mayor de edad")