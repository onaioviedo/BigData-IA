# Ejercicio 7. Ternaria: mensaje de resultado
# - Crea una variable nota con un valor numérico.
# - Usa un condicional ternario para guardar en resultado el texto Aprobado si la nota es mayor o igual que 5, o Suspenso en caso contrario.
# - Usa otro condicional ternario para guardar en tipo_nota el texto Alta si la nota es mayor o igual que 8, o Normal en caso contrario.
# - Muestra por consola la nota, el resultado y el tipo de nota.
# Condición:
# El ejercicio debe usar al menos dos expresiones ternarias.
 
nota = 8.5
resultado = "Aprobado" if nota >= 5 else "Suspenso"
tipo_nota = "Alta" if nota >= 8 else "Normal"
 
print(nota)
print(resultado)
print(tipo_nota)