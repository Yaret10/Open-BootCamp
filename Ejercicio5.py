#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def año_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return año , "Es bisiesto"
    else:
        return año , "No es bisiesto"
print(año_bisiesto(2000))

    

