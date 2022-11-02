import pandas as pd
import easygui as ventana

# Llamamos ventanas
mensaje = "Registro de pacientes del Hospital"
titulo  = "REGISTRO DE PACIENTES"

n_paciences = int(ventana.integerbox("Ingrese el número de pacientes a registrar: "))

lista = ["Nombre del paciente:", "Usuario del paciente: ", "Contraseña del usuario: ", "Fecha de nacimiento: ", "Sintomas del paciente: "]

pacience_name      = []
pacience_user      = []
pacience_password  = []
pacience_datebirth = []
pacience_symptom   = []

for i in range(0, n_paciences):
    ventana.msgbox(f'Paciente N°: {i+1}')
    caja = ventana.multenterbox(mensaje, titulo, lista)
    pacience_name.append(caja[0])
    pacience_user.append(caja[1])
    pacience_password.append(caja[2])
    pacience_datebirth.append(caja[3])
    pacience_symptom.append(caja[4])

df = pd.DataFrame({
    'Nombre'          : pacience_name,
    'Usuario'         : pacience_user,
    'Contraseña'      : pacience_password,
    'Fecha_nacimiento': pacience_datebirth,
    'Enfermedad'      : pacience_symptom
})

print(df)

