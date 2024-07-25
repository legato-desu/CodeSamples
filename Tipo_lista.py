# Las listas van entre [] y se pueden modificar
lista_1 = []
frutas = ["Fresa","Narajna","Mango","Pera",9,[1,2,3]]
# Posicion 5 sub lista 2
print(frutas[5][2])

# Listas son mutables [pueden cambiar]
frutas = ["Fresa","Narajna","Mango","Pera"]
# Agrega un nuevo elemento y reemplaza la posicion
frutas[3] = "Durazno"
print(frutas)

# Tuplas no son mutables (no cambian)
frutas = ("Fresa","Narajna","Mango","Pera")