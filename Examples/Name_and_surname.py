# Name and surname

"""
Write a program that asks for the first and last name of the
user. After the sample data has been entered by screen the 
string 'Hello {name} {last name}, nice to meet him!'
"""
name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
print(f"¡Hola {name.capitalize()} {last_name.capitalize()}, gusto en conocerle!")