# Types lists

"""
Create a program that manipulates a list in different ways
"""
# The lists go between [] and can be modified
list_1 = []
fruit = ["Fresa","Narajna","Mango","Pera",9,[1,2,3]]

# Posicion 5 sub lista 2
print(fruit[5][2])

# Lists are mutable [can change]
fruit = ["Fresa","Narajna","Mango","Pera"]

# Add a new element and replace the position
fruit[3] = "Durazno"
print(fruit)

# Tuples are not mutable (they do not change)
fruit = ("Fresa","Narajna","Mango","Pera")