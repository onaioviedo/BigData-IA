# Ejercicio 1. Control de notas 
# Crea una lista llamada notas con al menos 10 calificaciones numéricas. 
# El programa debe: 
# - Mostrar todas las notas. 
# - Calcular cuántas notas están aprobadas y cuántas suspendidas. 
# - Calcular la nota media. 
# - Mostrar la nota más alta y la nota más baja. 
# - Indicar si la media final está aprobada o suspendida. 
# Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales. 

print("Solución del ejercicio 1")

notas = [10, 8, 2, 9, 6.6, 6.2, 7.1, 3, 0.2, 5]
for nota in notas:
    print(nota)

contAp = 0
contSusp = 0
for nota in notas:
    if nota >= 5:
        contAp += 1
    else:
        contSusp += 1
print("Num aprobados: ",contAp)
print("Num aprobados: ",contSusp)

cont = 0
suma = 0
media = 0
for nota in notas:
    suma += nota
    cont += 1
media = suma/cont
print("Media: ", round(media, 2))

max = 0
min = 10
for nota in notas:
    if nota > max:
        max = nota

for nota in notas:
    if nota < min:
        min = nota
print("Nota més alta: ", max)
print("Nota més baixa: ", min)

if media >= 5:
    print("Media de clase aprobada! Con: ", round(media, 2))
else:
    print("Media de clase suspendida! Con: ", round(media, 2))

# Ejercicio 2. Carrito de la compra 
# Crea dos listas: una con nombres de productos y otra con sus precios. 
# productos = ["pan", "leche", "arroz", "huevos"] 
# precios = [1.20, 0.95, 2.10, 2.80]
# El programa debe: 
# - Mostrar cada producto con su precio. 
# - Calcular el precio total de la compra. 
# - Aplicar un descuento del 10% si el total supera 20 euros. 
# - Mostrar el total final que debe pagarse. 
# Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos.

print("Solución del ejercicio 2")

productos = ["pan", "leche", "arroz", "huevos"] 
precios = [1.20, 0.95, 20.10, 2.80]

total = 0

for producto, precio in zip(productos, precios):
    print(producto, precio)
    total += precio

if total >= 20:
    total = total - (total * 0.1)

print("Total a pagar: ", total)

# Ejercicio 3. Registro de alumno 
# Crea un diccionario llamado alumno con los siguientes datos: 
# nombre 
# edad 
# curso 
# nota_media 
# faltas
# El programa debe: 
# - Mostrar todos los datos del alumno. 
# - Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5. - Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas. 
# - Mostrar un mensaje final combinando el resultado académico y el aviso por faltas. Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos.

print("Solución del ejercicio 3")

alumno = {
    "nombre": "Cristian",
    "edad": 22,
    "curso": "DAW-BIO",
    "nota_media": 3.3,
    "faltas": 20
}
msj = ""
for clave, valor in alumno.items():
    print(clave, ":", valor)

if alumno["nota_media"] >= 5:
    estado_académico = "Aprobado!"
else:
    estado_académico = "Suspendido!"

if alumno["faltas"] > 10:
    msj = alumno["nombre"],"debe recibir un aviso!"

print("Resultado académico: ",alumno["nota_media"], "\n",
      msj)

# Ejercicio 4. Números pares, impares y múltiplos 
# Usando range, recorre los números del 1 al 50. 
# El programa debe: 
# - Contar cuántos números son pares. 
# - Contar cuántos números son impares. 
# - Contar cuántos números son múltiplos de 5. 
# - Mostrar los tres resultados finales. 
# Condición: Debe utilizar for, range, el operador módulo % y contadores. 

print("Solución del ejercicio 4")

contPar = 0
contImp = 0
contMult5 = 0
for i in range(1, 50):
    print(i)
    if i % 2 == 0:
        contPar += 1
    else:
        contImp += 1

    if i % 5 == 0:
        contMult5 += 1

print("Numero de pares:",contPar)
print("Numero de impares:",contImp)
print("Numero de múltiplos de 5:",contMult5)

# Ejercicio 5. Validación de contraseña 
# Crea una variable llamada password con una contraseña de prueba. 
# El programa debe: 
# - Comprobar si la contraseña tiene al menos 8 caracteres. 
# - Comprobar si contiene el símbolo @. 
# - Comprobar que no sea igual a 12345678. 
# - Si cumple todas las condiciones, mostrar Contraseña válida. 
# - En caso contrario, mostrar Contraseña no válida. 
# Condición: Debe utilizar strings, len, operadores lógicos y condicionales. Para comprobar si aparece @ dentro del texto puede utilizarse "@" in password. 

print("Solución del ejercicio 5")

password = "alv89tela66"

if len(password) > 8:
    if "@" in password:
        if password != "12345678":
            print("Contraseña vàlida!")
        else:
            print("Contraseña ivalida")
    else:
        print("Contraseña ivalida")
else:
    print("Contraseña ivalida")

# Ejercicio 6. Inventario de productos 
# Crea un diccionario donde las claves sean nombres de productos y los valores sean las unidades disponibles. 
# inventario = { 
#  "ratón": 12, 
#  "teclado": 5, 
#  "monitor": 0, 
#  "cable": 25 
# }

# El programa debe: 
# - Mostrar todos los productos y sus unidades. 
# - Mostrar qué productos están agotados. 
# - Calcular cuántas unidades hay en total. 
# - Mostrar cuántos productos tienen menos de 10 unidades. 
# Condición: Debe utilizar diccionarios, items(), acumuladores, contadores e if. 


print("Solución del ejercicio 6")

inventario = { 
 "ratón": 12, 
 "teclado": 5, 
 "monitor": 0, 
 "cable": 25 
}

for clave, valor in inventario.items():
    print(clave, "quedan", valor, "unidades")

for clave, valor in inventario.items():
    if valor == 0:
        print(clave, "está agotado!")

total = 0
for valor in inventario.values():
    total += valor
print("Total de unidades: ", total)

for clave, valor in inventario.items():
    if valor < 10:
        print(clave, "tiene menos de 10 unidades!") 

# Ejercicio 7. Búsqueda en una lista 
# Crea una lista de nombres de alumnos y una variable con el nombre que se quiere buscar. El programa debe: 
# - Recorrer la lista buscando ese nombre. 
# - Si encuentra el nombre, mostrar en qué posición está. 
# - Cuando lo encuentre, detener la búsqueda. 
# - Si no lo encuentra, mostrar Alumno no encontrado. 
# Condición: Debe utilizar listas, for, enumerate, if, break y una variable booleana de control.

lista = ["Cristian", "Javier", "Alvaro", "David", "Jorge"]
nombre_a_buscar = "Alvaro"
encontrado = False

for i, nombre in enumerate(lista):
    if nombre == nombre_a_buscar:
        print(f"{nombre_a_buscar} está en la posición {i}")
        encontrado = True
        break

if not encontrado:
    print("Alumno no encontrado")

# Ejercicio 8. Limpieza de datos 
# Crea una lista con varios números, incluyendo positivos, negativos y ceros. 
# El programa debe: 
# - Recorrer la lista completa. 
# - Ignorar los números negativos usando continue. 
# - Sumar solo los números positivos. 
# - Contar cuántos ceros hay. 
# - Mostrar la suma final y la cantidad de ceros. 
# Condición: Debe utilizar listas, for, continue, un acumulador y un contador. 

print("Solución del ejercicio 8")   

numeros = [1, -2, 3, 0, -5, 0, 7, -1]

suma = 0
contCeros = 0
for num in numeros:
    if num < 0:
        continue
    elif num == 0:
        contCeros += 1
    else:
        suma += num

print("Suma final:", suma)
print("Cantidad de ceros:", contCeros)

# Ejercicio 9. Clasificación de usuarios 
# Crea una lista de diccionarios. Cada diccionario representa un usuario con los siguientes datos: 
# nombre 
# edad 
# activo 
# puntos

# El programa debe: 
# - Clasificar como Premium a los usuarios activos con 100 puntos o más. 
# - Clasificar como Estándar a los usuarios activos con menos de 100 puntos. 
# - Clasificar como Inactivo a los usuarios que no estén activos. 
# - Además, si el usuario es menor de 18 años, debe indicarse como usuario menor de edad. 
# - Mostrar el nombre de cada usuario y su clasificación. 
# Condición: Debe utilizar una lista de diccionarios, bucle for, booleanos, if, elif, else y operadores lógicos. 

print("Solución del ejercicio 9")

usuarios = [
    {"nombre": "Cristian", "edad": 22, "activo": True, "puntos": 150},
    {"nombre": "Javier", "edad": 17, "activo": True, "puntos": 80},
    {"nombre": "Alvaro", "edad": 25, "activo": False, "puntos": 50},
    {"nombre": "David", "edad": 30, "activo": True, "puntos": 90},
    {"nombre": "Jorge", "edad": 16, "activo": False, "puntos": 120}
]

for usuario in usuarios:
    if not usuario["activo"]:
        clasificacion = "Inactivo"
    elif usuario["puntos"] >= 100:
        clasificacion = "Premium"
    else:
        clasificacion = "Estándar"

    if usuario["edad"] < 18:
        clasificacion += " (menor de edad)"

    print(f"{usuario['nombre']}: {clasificacion}")

# Ejercicio 10. Sistema de intentos 
# Crea una variable codigo_correcto y una lista llamada intentos con varios códigos introducidos. El programa debe: 
# - Recorrer todos los intentos. 
# - Mostrar cada intento realizado. 
# - Si un intento está vacío, debe entrar en una condición donde se use pass como marcador. - Si un intento coincide con el código correcto, mostrar Acceso concedido y terminar el bucle. 
# - Si después de todos los intentos no se encuentra el código correcto, mostrar Acceso denegado. Condición: Debe utilizar listas, for, if, elif, else, break, pass, una variable booleana y un condicional 

print("Solución del ejercicio 10")

codigo_correcto = "1234"
intentos = ["0000", "", "1111", "1234", "2222"]
acceso_concedido = False    

for intento in intentos:
    if intento == "":
        pass
    elif intento == codigo_correcto:
        print("Acceso concedido")
        acceso_concedido = True
        break
    else:
        print(f"Intento: {intento}")

if not acceso_concedido:
    print("Acceso denegado")