# Operadores aritméticos (+,-,*,/,%,**,//)

numero1 = 5
numero2 = 2

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f'Primer número: {numero1}')
print(f'Segundo número: {numero2}')
print('Suma:           {n1} + {n2} = {s}'.format(n1=numero1, n2=numero2, s=suma))
print('Resta:          {n1} - {n2} = {r}'.format(n1=numero1, n2=numero2, r=resta))
print('Multiplicación: {n1} * {n2} = {m}'.format(n1=numero1, n2=numero2, m=multiplicacion))
print('División:       {n1} / {n2} = {d}'.format(n1=numero1, n2=numero2, d=division))

# Operador de resto %
resto = numero1 % numero2

# Operador de cociente //
cociente = numero1 // numero2

# Operador de potencia **
potencia = numero1 ** numero2

print('Resto:          {n1} % {n2} = {re}'.format(n1=numero1, n2=numero2, re=resto))
print('Cociente:       {n1} // {n2} = {c}'.format(n1=numero1, n2=numero2, c=cociente))
print('Potencia:       {n1} ** {n2} = {p}'.format(n1=numero1, n2=numero2, p=potencia))
