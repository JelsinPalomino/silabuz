# Escriba un programa en Python para calcular el número de días entre dos fechas. 
# No es necesario que use inputs para el ingreso de las fechas.

from datetime import datetime
import datetime

firstD  = datetime.date(2022, 12, 1)
secondD = datetime.date(2022, 12, 12)
daysD   = secondD - firstD
print(daysD.days)