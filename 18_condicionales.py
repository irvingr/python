# Condiciones (if, elif, else)

a = 8
b = 3
c= 4
d = 6

# IF
if (a > b):
    print("a es mayor que b")

if (a > c) and (b < d): # La condición se cumple
    print("La primera expresión es correcta - a es mayor que c y b es menor que d")

if (a > c) and (b > d):
    print("La primera expresión es correcta")

# ELSE

if(a > c) and (b > d):
    print("La primera expresión es correcta")
else:
    print("La primera expresión NO es correcta")

# ELIF
if (a < b):
    print("a es mayor que b")
elif (a == b):
    print("a es igual que b")
else:
    print("Ninguna expresion anterior es correcta")