# Merge lists

"""
Create a program that merges lists with different methods
"""
list_1 = [1,2,3]
list_2 = [4,5,6,7]
fruit_list = ["Fresa","Mango","Pera"]

# Con simbolo +
Union_1 = list_1 + list_2 + fruit_list
# Metodo extend()
list_1.extend(list_2)
list_1.extend(fruit_list)

print(f"Con '+' = {Union_1}")
print(f"Con 'extend' = {list_1}")