# Operadores lógicos (and, or, not)

numero1 = 10
numero2 = 4
numero3 = 7
numero4 = 3

print('- - - > and - or - not < - - -')
# Operador and
print(f'({numero1} < {numero2}) and ({numero3} > {numero4}) . . . {(numero1 < numero2) and (numero3 > numero4)}')

# Operador or
print(f'({numero1} < {numero2}) or ({numero3} > {numero4}) . . . {(numero1 < numero2) or (numero3 > numero4)}')

# Operador not
print(f'not({numero3} > {numero4}) . . . {not(numero3>numero4)}')