# Ejercicio 9. Caso completo: pedido online
# - Crea una lista llamada productos con tres productos.
# - Crea una lista llamada precios con tres precios, en el mismo orden que los productos.
# - Crea un diccionario llamado cliente con las claves nombre, es_socio y saldo.
# - Crea un conjunto llamado cupones_validos con tres códigos de cupón.
# - Crea una variable cupon_usado con uno de esos códigos o con un código inventado.
# - Calcula el total del pedido sumando los tres precios.
# - Crea una variable tiene_descuento que sea True si el cliente es socio o si el cupón usado está en cupones_validos.
# - Si tiene_descuento es True, calcula total_final aplicando un descuento del 10%. Si no, total_final será igual al total.
# - Si el saldo del cliente es mayor o igual que total_final, el mensaje será Pedido aceptado. En caso contrario, será Saldo insuficiente.
# - Muestra por consola el nombre del cliente, productos, total_final y mensaje.
# Condición:
# Debe mezclar listas, diccionarios, conjuntos, operadores aritméticos, operadores lógicos y condicionales.
 
productos = ["Portátil", "Ratón", "Teclado"]
precios = [800, 25, 45]
cliente = {"nombre": "Onai", "es_socio": False, "saldo": 900}
cupones_validos = {"DESC10", "VERANO", "PROMO"}
cupon_usado = "VERANO"
 
total = precios[0] + precios[1] + precios[2]
tiene_descuento = cliente["es_socio"] or cupon_usado in cupones_validos
 
if tiene_descuento:
    total_final = total * 0.9
else:
    total_final = total
 
if cliente["saldo"] >= total_final:
    mensaje = "Pedido aceptado"
else:
    mensaje = "Saldo insuficiente"
 
print(cliente["nombre"])
print(productos)
print(total_final)
print(mensaje)