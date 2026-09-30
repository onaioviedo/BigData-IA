#Ejercicio 2. Tuplas: datos fijos de un producto
#- Crea una tupla llamada producto con tres datos: nombre del producto, precio y unidades disponibles.
#- Por ejemplo: ("teclado", 25.50, 12).
#- Guarda cada dato de la tupla en una variable diferente: nombre, precio y unidades.
#- Calcula el valor total del stock multiplicando precio por unidades.
#- Muestra por consola el nombre del producto, el precio, las unidades y el valor total del stock.
#Condición:
#Debe utilizar: tupla, acceso por índice y operaciones aritméticas sencillas.


producto = ("libreta", 4.99, 56)


nombre = producto(0)
precio = producto(1)
unidades = producto(2)


valorStock = precio * unidades


print(valorStock)
