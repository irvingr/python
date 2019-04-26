# Operadores de pertenencia (in, not in)

escuderias = ['Mercedes', 'Ferrari', 'Red Bull']
escuderia1 = 'Ferrari'
escuderia2 = 'BMW'

# IN

# El elemento Ferrari si pertenece a escuderias - Verdadero
print(escuderia1 in escuderias) # True
# El elemento Ferrari no pertenece a escuderias - Falso
print(escuderia1 not in escuderias) # False

# NOT IN

# El elemento BMW no pertenece a escuderias - Verdadero
print(escuderia2 not in escuderias) # True

# El elemento BMW pertenece a escuderias - Falso
print(escuderia2 in escuderias) # False