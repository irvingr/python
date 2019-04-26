# Funciones - Bloque de código que se ejecuta cuando es llamado

def saludar():
    print("Buenos días")

# Invoca a la función saludar.
saludar() # Buenos días

def saludo(nombre):
    print("Buenos días " + nombre)

nombre = "José"
# Invoca a la función saludo.
saludo(nombre) # Buenos días José

def sumar(numero1, numnero2):
    suma = numero1 + numero2
    return suma

numero1 = 3
numero2 = 6
resultado = sumar(numero1, numero2) # Invoca a la función sumar.
print(resultado) # 9

# Paso de valor por referencia.
colores = ["rojo", "verde", "azul"]

def incluir_color(colores, color):
    colores.append(color)

color = "morado"
incluir_color(colores, color)

print(colores) # ['rojo', 'verde', 'azul', 'morado']