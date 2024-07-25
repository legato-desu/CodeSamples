edad = input("Ingrese su edad: ")

# Evalua que si sea un numero entero
try:
    edad = int(edad)
except:
    print("Ingrese una edad valida") 
    exit()

# Enseña por pantalla la edad    
if edad >= 18:
    print("Eres mayor de edad")
