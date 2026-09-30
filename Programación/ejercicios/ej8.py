# Ejercicio 8. match-case: menú de aplicación
# - Crea una variable opcion con un texto: crear, editar, borrar, listar u otra opción.
# - Crea una variable mensaje.
# - Usa match-case para asignar un mensaje distinto según la opción elegida.
# - Si opcion es "crear", mensaje debe ser Creando registro.
# - Si opcion es "editar", mensaje debe ser Editando registro.
# - Si opcion es "borrar", mensaje debe ser Borrando registro.
# - Si opcion es "listar", mensaje debe ser Mostrando registros.
# - Para cualquier otro valor, mensaje debe ser Opción no reconocida.
# - Muestra por consola el valor de mensaje.
# Condición:
# Debe incluirse un case _ como opción por defecto.
 
opcion = "editar"
 
match opcion:
    case "crear":
        mensaje = "Creando registro"
    case "editar":
        mensaje = "Editando registro"
    case "borrar":
        mensaje = "Borrando registro"
    case "listar":
        mensaje = "Mostrando registros"
    case _:
        mensaje = "Opción no reconocida"
 
print(mensaje)