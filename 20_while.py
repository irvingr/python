# while

valor = 1
fin = 10

while (valor < fin):
    print(valor)
    valor += 1

print("- - - - - - - - - BREAK - - - - - - - - - -")

# break
valor = 1
fin = 10

while (valor < fin):
    print(valor)
    valor += 1
    if (valor == 5):
        break

print("- - - - - - - - - CONTINUE - - - - - - - - - -")

# continue
valor = 1
fin = 10

while (valor < fin):
    valor += 1
    if (valor == 7):
        continue
    print(valor)