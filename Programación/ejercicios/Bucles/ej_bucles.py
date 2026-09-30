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