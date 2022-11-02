# Escriba un programa de Python para listar todos los archivos en un directorio en Python. 
# (por precaución que sea en una carpeta temporal y que no contenga archivos importantes, coloque copias)

import pathlib

# Creen una carpeta cualquiera y agreguen archivos de diversas extensiones

direct_music = 'C:/Users/Nicki/Music/Musica/'
directM      = pathlib.Path(direct_music)

for file in directM.iterdir():
    print(file.name)