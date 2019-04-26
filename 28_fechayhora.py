# Fecha y hora

from datetime import datetime

fechayhora = datetime.now()

print(fechayhora)

anio = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

# hora

hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

print("La hora es {}:{}:{}".format(hora, minutos, segundos))