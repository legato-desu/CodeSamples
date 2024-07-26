# Switch

"""
Create a program that asks the user for a number from 1 to 4 and displays it on the screen. 
What station does that number correspond to?
"""
print("\nEstaciones del año")
print("==================\n")
season = int(input("Ingrese un numero de 1 a 4: "))
match season:
    case 1:
        print(f"La {season}° estacion es: Primavera")
    case 2:
        print(f"La {season}° estacion es: Verano")
    case 3:
        print(f"La {season}° estacion es: Otoño")
    case 4:
        print(f"La {season}° estacion es: Invierno")
    case _:
        print("No es un numero valido")