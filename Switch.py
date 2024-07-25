"""
Por último, para el Switch, deberás crear la variable estacion, y distintos case 
para las cuatro estaciones del año. Dependiendo del valor de la variable estacion 
se deberá mandar un mensaje por consola informando de la estación en la que está. 
También habrá que poner un default para cuando el valor de la variable no sea una 
estación.
"""
estacion = 'otoño'

match estacion:
    case 'primavera':
        print('La estacion es: primavera')
    case 'verano':
        print('La estacion es: verano')
    case 'otoño':
        print('La estacion es: otoño')
    case 'invierno':
        print('La estacion es: invierno')
    case _:
        print('No es una estacion valida')