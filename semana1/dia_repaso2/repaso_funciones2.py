"""
hallar el pago semanal de los trabajadores de la empresa x, 
la cual debe de ingresar el numero de horas y el pago por 
hora, el pago semanal es el siguiente : pago normal: ph * ht 
, si tiene  mas de 40 horas y menos o igual a 48 las que exceden 
de 40 se les paga el doble por cada hora , si tienen mas de 48,
las que exceden de 48 se les paga el triple por cada hora

"""
"""
def pay_week1(hours, pay_hours):
    pay_week=0
    if hours <= 40:
        pay_week = hours*pay_hours
    elif hours >= 40 and hours <= 48:
        pay_week = pay_week + (hours-40) * (2*pay_hours)
        modalidad = "doble de pago por hora extra"
    elif hours >= 48:
        pay_week = pay_week + (hours-48) * (3*pay_hours)
        modalidad = "triple de pago por hora extra"
    print(f"El pago semanal a los trabajadores de la empresa x es {pay_week} por la modalidad: {modalidad}")

hours = int(input("Ingresar el numero de horas: "))
pay_hours = int(input("Pago por hora: "))

print(pay_week1(hours, pay_hours))
"""

"""
ht=int(input("Ingresar las horas trabajadas: "))
ph=float(input("Ingresar el pago por hora: "))

def pago(a,b):

    if ht<40:
        pago=a*b
        return pago

    elif 40<=a<=48:
        pago=b*(40+2*(ht-40))
        return pago

    elif a>48:
        pago=b*(40+3*(ht-40))
        return pago

    else:
        return None

resultado=pago(ht,ph)
print(resultado)

"""
