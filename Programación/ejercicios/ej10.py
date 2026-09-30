# Ejercicio 10. Caso completo: evaluación de acceso
# - Crea una tupla llamada requisitos con tres valores: edad mínima, nota mínima y si se requiere permiso.
# - Ejemplo: requisitos = (18, 6, True).
# - Crea un diccionario llamado candidato con las claves nombre, edad, nota y permiso.
# - Crea un conjunto llamado cursos_disponibles con tres cursos.
# - Crea una variable curso_elegido.
# - Crea una variable curso_existe que compruebe si curso_elegido está en cursos_disponibles.
# - Crea una variable cumple_edad comparando la edad del candidato con la edad mínima.
# - Crea una variable cumple_nota comparando la nota del candidato con la nota mínima.
# - Crea una variable cumple_permiso. Si el requisito de permiso es True, debe comprobarse el permiso del candidato. Si no se requiere permiso, debe valer True.
# - Usa if, elif y else para crear un mensaje final: Acceso concedido, Curso no disponible, No cumple requisitos o Solicitud incompleta.
# - Usa una ternaria para crear un estado breve: Apto si el mensaje final es Acceso concedido, o No apto en caso contrario.
# - Muestra por consola el nombre del candidato, el curso elegido, el estado breve y el mensaje final.
# Condición:
# Debe combinar tuplas, diccionarios, conjuntos, condiciones múltiples, if/elif/else y ternaria.
 
requisitos = (18, 6, True)
candidato = {"nombre": "Marta", "edad": 20, "nota": 7, "permiso": True}
cursos_disponibles = {"Python", "Java", "SQL"}
curso_elegido = "Python"
 
curso_existe = curso_elegido in cursos_disponibles
cumple_edad = candidato["edad"] >= requisitos[0]
cumple_nota = candidato["nota"] >= requisitos[1]
 
if requisitos[2]:
    cumple_permiso = candidato["permiso"]
else:
    cumple_permiso = True
 
if not curso_elegido or not candidato["nombre"]:
    mensaje_final = "Solicitud incompleta"
elif not curso_existe:
    mensaje_final = "Curso no disponible"
elif cumple_edad and cumple_nota and cumple_permiso:
    mensaje_final = "Acceso concedido"
else:
    mensaje_final = "No cumple requisitos"
 
estado = "Apto" if mensaje_final == "Acceso concedido" else "No apto"
 
print(candidato["nombre"])
print(curso_elegido)
print(estado)
print(mensaje_final)