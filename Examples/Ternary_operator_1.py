# Ternary operator 1

"""
Develop a program that asks the user for a number and if it is even, cube it, 
and if it is odd squared
"""
number = int(input("Ingrese un numero: "))
power = number**3 if (number%2)==0 else number**2
print(f"Su resultado es: {power}")