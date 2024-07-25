# Delete element

"""
Create a program that deletes an item contained in a list
"""
country = ["Peru","Brasil","Argentina","Ecuador", "Uruguay", 
        "Chile", "Bolivia", "Colombia", "Venezuela"]
print(country)
# Method DEL
del(country[4])
print(country)
# Method REMOVE
country.remove("Chile")
print(country)
# Method POP
grd_country = country.pop(4)
print(grd_country)
print(country)