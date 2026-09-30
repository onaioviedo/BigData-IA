# Ejercicio 5. Condiciones con and, or y not
# - Crea las variables edad, tiene_permiso, es_socio y sancionado.
# - Asigna valores concretos a esas variables.
# - Crea una variable acceso_por_edad que sea True si la persona tiene al menos 16 años y tiene permiso.
# - Crea una variable acceso_por_socio que sea True si la persona es socio y no está sancionada.
# - Crea una variable puede_acceder que sea True si se cumple acceso_por_edad o acceso_por_socio.
# - Muestra por consola las tres variables: acceso_por_edad, acceso_por_socio y puede_acceder.
# Condición:
# La condición final debe utilizar and, or y not.
 
edad = 17
tiene_permiso = True
es_socio = False
sancionado = False
 
acceso_por_edad = edad >= 16 and tiene_permiso
acceso_por_socio = es_socio and not sancionado
puede_acceder = acceso_por_edad or acceso_por_socio
 
print(acceso_por_edad)
print(acceso_por_socio)
print(puede_acceder)