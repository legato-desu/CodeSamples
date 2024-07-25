# If

"""
Using an if, create a condition that compares whether the variable numberIf 
is positive, negative, or 0. Hint: Numbers less than 0 are negative 
and numbers greater than 0 are positive.
"""
numberif = int(input('Ingrese el numero a evaluar: '))
if (numberif > 0):
    print(f"El numero {numberif} es positivo")
elif(numberif < 0):
    print(f"El numero {numberif} es negativo")
else:
    print(f"El numero es cero (0)")