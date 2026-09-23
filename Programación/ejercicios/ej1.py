#Ejercicio 1. Listas: control de notas
#- Crea una lista llamada notas con cinco calificaciones: 6, 8, 5, 9 y 7.
#- Guarda en una variable primera_nota el primer elemento de la lista.
#- Guarda en una variable ultima_nota el último elemento de la lista.
#- Cambia la segunda nota de la lista por un 10.
#- Añade una nueva nota, 8, al final de la lista.
#- Guarda en una variable total_notas la cantidad de notas que hay en la lista.
#- Muestra por consola la lista final, la primera nota, la última nota y el total de notas.

notas = [6, 8, 5, 9, 7]

primer_nota = notas[0]

ultima_nota = notas[4]

notas[1] = 10

notas.append(8)

total_notas = len(notas) 

print(notas)
print(primer_nota)
print(ultima_nota)
print(total_notas)