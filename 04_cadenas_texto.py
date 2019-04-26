cadena = 'Hello world'
print(cadena)
print()
# H e l l o   w o r l d
# 0 1 2 3 4 5 6 7 8 9 10

string = "H e l l o   w o r l d  <=  String"
posStr = "0 1 2 3 4 5 6 7 8 9 10 <=  Posición string"

cadena1 = "Hello"
cadena2 = " "
cadena3 = "world"

print(string)
print(posStr)
print()
print(cadena[4],' <=  pos #4')
print(cadena[-1],' <= última posición -1')
print(cadena[2:7],' <= inicia desde pos #2 y termina antes de pos #7')
print(cadena[2:],' <= inicia desde pos #2 hasta el final')
print(cadena[8],' <= pos #8')

# Concatenación 
cadenafinal = cadena1 + cadena2 + cadena3
print(cadenafinal,' <= concatenación de cadenas')
