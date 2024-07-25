# Sort lists

"""
Create a program to sort the values in the list
according to their values "if they are characters - alphabetical" and if 
"they are numbers - growing"
"""
fruit = ["Naranja","Fresa","Mango","Pera"]
numbers = {7,9,1,3,0,2,8,6,4,5}

# Sort () ordena alfabeticamente Ascendente  "reverse=True" Descendente
fruit.sort() # Ascendente
fruit.sort(reverse=True) # Descendente
print(fruit)

# Reverse()   Invierte la lista primero a ultimo y ultimo a primero
fruit.reverse()
print(fruit)

# Sorted()   Si devuelve la lista ordenada
sorted_list_1 = sorted(numbers)
sorted_list_2 = sorted(numbers,reverse=True)
print(sorted_list_1)
print(sorted_list_2)