import easygui as ventana

mensaje = "Calculo del precio total de una compra"
titulo  = "Factura total"

lista =["Precio del producto: ", "Cantidad del producto: ", "Impuesto en %: "]

caja = ventana.multenterbox(mensaje, titulo, lista)

# Calculamos
total = float(caja[0])*float(caja[1])
impuesto = total*float(caja[2])/100
totalReal = total*impuesto

# print(total, totalReal, impuesto)
"""
mensaje = "Total a pagar con impuestos: " + str(totalReal)

ventana.msgbox(mensaje, titulo, ok_button='OK')
"""

ventana.msgbox()