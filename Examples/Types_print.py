# Types print

"""
Create a program that uses different examples for screen messages
"""
# Basic use of the print function
print("Este es un ejemplo basico. ")

# The line break is canceled
print("Ejemplo sin saltar de linea. ",end="")
print("Ejemplo sin saltar de linea. ",end="")

print()
# Concatenate
print("Python ", "es ","genial")

# A (-) is added to the spaces
print("Python ", "es ","genial", sep="-")

print()
# Using the format function
print ("{} es {}".format("Python","genial"))

number = [2,3,5,7,11]
print(number)

capitals = {"Colombia":"Bogota","Peru":"Lima"}
print(capitals)