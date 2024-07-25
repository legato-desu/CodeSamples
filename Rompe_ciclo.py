"""
break: detiene o rompe la ejecucion del ciclo
continue: salta a la siguiente interacion del ciclo
"""
lista_frutas = ["Fresa","Naranja","Mango","Pera"]

for fruta in lista_frutas:
    if fruta == "Mango":
        continue
    print(fruta)