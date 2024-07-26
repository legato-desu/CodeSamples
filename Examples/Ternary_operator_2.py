# Ternary operator 2

"""
Write a program that asks two users for their name and age and 
print the name of the eldest
"""
user_1 = input("Nombre del primer usuario: ")
age_1 = int(input("Edad del primer usuario: "))

user_2 = input("Nombre del segundo usuario: ")
age_2 = int(input("Edad del segundo usuario: "))

print(f"{user_1.capitalize()} es mayor")if age_1 > age_2 else print(f"{user_2.capitalize()} es mayor")