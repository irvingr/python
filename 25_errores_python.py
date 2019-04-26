# try ... except ... else ... finally

# TRY - EXCEPT
print("-- Try/Except")
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    
    print(division)
except:
    print("Ha habido un error")

# ZeroDivisionError
print("-- ZeroDivisionError")
try:
    num1 = 56
    num2 = 7

    division =  num1 / num2

    print(division)
except ZeroDivisionError:
    print("Error, división entre cero")
except:
    print("Ha habido un error")
else:
    print("La división funcionó correctamente")

# finally - siempre se ejecuta independientemente del try y except
print("-- Finally")
try:
    n1 = 8
    n2 = 2

    division = n1 / n2
    print(division)
except ZeroDivisionError:
    print("Error, división entre cero")
except:
    print("Ha habido un error")
else:
    print("La división funcionó correctamente")
finally:
    print("Esta prueba del try ha terminado")



