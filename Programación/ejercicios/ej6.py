# Ejercicio 6. if, elif y else: clasificación de matrícula
# - Crea las variables nota_media, renta_baja y familia_numerosa.
# - Asigna valores concretos a esas variables.
# - Crea una variable mensaje.
# - Si la nota_media es menor que 5, mensaje debe ser No admitido.
# - Si la nota_media es mayor o igual que 9, mensaje debe ser Beca completa.
# - Si la nota_media es mayor o igual que 7 y además renta_baja o familia_numerosa es True, mensaje debe ser Beca parcial.
# - Si la nota_media es mayor o igual que 5, mensaje debe ser Admitido sin beca.
# - En cualquier otro caso, mensaje debe ser Revisar solicitud.
# - Muestra por consola el valor final de mensaje.
# Condición:
# Debe resolverse con una estructura que combine if, varios elif y else.
 
nota_media = 7.5
renta_baja = True
familia_numerosa = False
 
if nota_media < 5:
    mensaje = "No admitido"
elif nota_media >= 9:
    mensaje = "Beca completa"
elif nota_media >= 7 and (renta_baja or familia_numerosa):
    mensaje = "Beca parcial"
elif nota_media >= 5:
    mensaje = "Admitido sin beca"
else:
    mensaje = "Revisar solicitud"
 
print(mensaje)