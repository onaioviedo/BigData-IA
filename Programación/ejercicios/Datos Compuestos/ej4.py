# Ejercicio 4. Conjuntos: usuarios registrados
# - Crea un conjunto llamado usuarios con estos nombres: Ana, Luis, Marta, Ana y Pedro.
# - Crea una variable nuevo_usuario con el valor "Luis".
# - Crea una variable usuario_existe que compruebe si nuevo_usuario está dentro del conjunto.
# - Añade el usuario "Clara" al conjunto.
# - Crea una variable total_usuarios con el número de usuarios únicos.
# - Muestra por consola el conjunto final, usuario_existe y total_usuarios.
# Condición:
# Debe utilizar: conjunto, eliminación automática de duplicados, pertenencia con in y len.


usuarios = {"Ana", "Luis", "Marta", "Ana", "Pedro"}


nuevo_usuario = "Luis"


usuario_existe = nuevo_usuario in usuarios


usuarios.add("Clara")


total_usuarios = usuarios.len


print(usuario_existe)
print(total_usuarios)
