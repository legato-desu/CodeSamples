# Conditional cycle

"""
break: stops or breaks the execution of the loop
continue: jump to the next interaction in the loop
"""
fruit_list = ["Fresa","Naranja","Mango","Pera"]

for fruit in fruit_list:
    if fruit == "Mango":
        continue
    print(fruit)