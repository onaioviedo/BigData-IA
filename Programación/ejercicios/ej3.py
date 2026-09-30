# Ejercicio 3. Diccionarios: ficha de alumno
# - Crea un diccionario llamado alumno.
# - El diccionario debe tener estas claves: nombre, edad, curso y nota.
# - Usa valores concretos, por ejemplo: "Ana", 16, "IA" y 7.5.
# - Muestra por consola el nombre del alumno usando la clave nombre.
# - Muestra por consola la nota del alumno usando la clave nota.
# - Cambia la nota del alumno por otro valor.
# - Añade una nueva clave llamada aprobado. Su valor debe ser el resultado de comprobar si la nota es mayor o igual que 5.
# - Muestra por consola el diccionario completo al final.
# Condición:
# Debe utilizar: diccionario, claves de texto, consulta de valores, modificación y creación de una nueva clave.




alumno = {
    "nombre": "Ana",
    "edad": 16,
    "curso": "IA",
    "nota": 7.5
}


print(alumno["nombre"])
print(alumno["nota"])


alumno["nota"] = 3.2


alumno["aprobado"] == True


if alumno["nota"] >= 5:
    alumno["aprobado"] == True
else:
    alumno["aprobado"] == False


print(alumno)
