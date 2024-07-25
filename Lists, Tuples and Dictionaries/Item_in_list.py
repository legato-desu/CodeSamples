# Item in list

"""
Create a program where the user is asked for a country and looks to see if that country is
in the established list or not
"""
country = input("Ingrese el nombre de el pais: ")
country = country.capitalize()
country_list = ["Peru","Brasil","Argentina","Ecuador", "Uruguay", "Chile", "Bolivia", "Colombia", "Venezuela"]
if country in country_list:
    print(f"El pais {country} si esta en la lista")
else:
    print(f"El pais {country} no esta en la lista")