import math
import pandas as pd


def coinciden(a, b, c):
    """Comprueba si tres valores (o tres listas de valores) coinciden."""
    if isinstance(a, list):
        return all(
            math.isclose(x, y, abs_tol=1e-9) and math.isclose(x, z, abs_tol=1e-9)
            for x, y, z in zip(a, b, c)
        ) and len(a) == len(b) == len(c)
    return math.isclose(a, b, abs_tol=1e-9) and math.isclose(a, c, abs_tol=1e-9)


# =====================================================================
print("Solución del ejercicio 1")
# =====================================================================
# Carga y exploración de datos
df = pd.read_csv("datos_estadistica_alumnos.csv")
print(df.head())

puntos = list(df["puntos_prueba"])
print("Cantidad de datos en puntos_prueba:", len(puntos))
print("Explicación: cada fila del CSV representa a un alumno, con sus horas de "
      "estudio, los puntos obtenidos en la prueba, los ejercicios entregados y "
      "los minutos de uso de la plataforma.")
print()

# =====================================================================
print("Solución del ejercicio 2")
# =====================================================================
# Media: suma de todos los valores dividida entre la cantidad de datos
suma = 0
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)

media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

media_pandas = df["puntos_prueba"].mean()

print("media_bucle:", media_bucle)
print("media_funciones:", media_funciones)
print("media_pandas:", media_pandas)
print("¿Coinciden?", coinciden(media_bucle, media_funciones, media_pandas))
print("Explicación: la media es la nota promedio del grupo en la prueba; "
      "es el valor que tendrían todos si los puntos se repartieran por igual.")
print()

media = media_bucle  # la reutilizamos en los siguientes ejercicios

# =====================================================================
print("Solución del ejercicio 3")
# =====================================================================
# Mediana: valor central de los datos ordenados
ordenados = []
for valor in puntos:
    ordenados.append(valor)
# ordenación manual (burbuja) para no usar sorted() en el método 1
for i in range(len(ordenados)):
    for j in range(len(ordenados) - 1 - i):
        if ordenados[j] > ordenados[j + 1]:
            ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]
n = len(ordenados)
if n % 2 == 0:
    mediana_bucle = (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
else:
    mediana_bucle = ordenados[n // 2]

ordenados_f = sorted(puntos)
n_f = len(ordenados_f)
mediana_funciones = (
    (ordenados_f[n_f // 2 - 1] + ordenados_f[n_f // 2]) / 2
    if n_f % 2 == 0
    else ordenados_f[n_f // 2]
)

mediana_pandas = df["puntos_prueba"].median()

print("mediana_bucle:", mediana_bucle)
print("mediana_funciones:", mediana_funciones)
print("mediana_pandas:", mediana_pandas)
print("¿Coinciden?", coinciden(mediana_bucle, mediana_funciones, mediana_pandas))
print("Explicación: la mediana deja la mitad de los datos por debajo y la otra "
      "mitad por encima, por eso representa el centro y no le afectan los extremos.")
print()

# =====================================================================
print("Solución del ejercicio 4")
# =====================================================================
# Moda: valor que más se repite
frecuencias = {}
for valor in puntos:
    if valor in frecuencias:
        frecuencias[valor] += 1
    else:
        frecuencias[valor] = 1
moda_bucle = None
max_frec = 0
for valor, frec in frecuencias.items():
    if frec > max_frec:
        max_frec = frec
        moda_bucle = valor

moda_funciones = max(set(puntos), key=lambda x: puntos.count(x))

moda_pandas = df["puntos_prueba"].mode()[0]

print("moda_bucle:", moda_bucle)
print("moda_funciones:", moda_funciones)
print("moda_pandas:", moda_pandas)
print("¿Coinciden?", coinciden(moda_bucle, moda_funciones, moda_pandas))
print("Explicación: la moda es la puntuación más repetida; indica el resultado "
      "más habitual entre los alumnos.")
print()

# =====================================================================
print("Solución del ejercicio 5")
# =====================================================================
# Desviación de cada dato respecto a la media: punto - media
desviaciones_bucle = []
for punto in puntos:
    desviaciones_bucle.append(punto - media)

desviaciones_funciones = list(map(lambda x: x - media, puntos))

df["desviacion"] = df["puntos_prueba"] - media
desviaciones_pandas = list(df["desviacion"])

print("Método 1:", desviaciones_bucle)
print("Método 2:", desviaciones_funciones)
print("Método 3:", desviaciones_pandas)
print("¿Coinciden?", coinciden(desviaciones_bucle, desviaciones_funciones,
                               desviaciones_pandas))
print("Explicación: positiva = el alumno está por encima de la media; "
      "negativa = por debajo; cero = justo en la media.")
print()

# =====================================================================
print("Solución del ejercicio 6")
# =====================================================================
# Varianza poblacional: media de los cuadrados de las desviaciones (÷ n)
cuadrados = []
for punto in puntos:
    desv = punto - media
    cuadrados.append(desv ** 2)
suma_cuadrados = 0
for c in cuadrados:
    suma_cuadrados += c
varianza_bucle = suma_cuadrados / len(puntos)

varianza_funciones = sum(map(lambda x: (x - media) ** 2, puntos)) / len(puntos)

varianza_pandas = df["puntos_prueba"].var(ddof=0)

print("varianza_bucle:", varianza_bucle)
print("varianza_funciones:", varianza_funciones)
print("varianza_pandas:", varianza_pandas)
print("¿Coinciden?", coinciden(varianza_bucle, varianza_funciones, varianza_pandas))
print("Explicación: la varianza mide cuánto se dispersan las notas respecto a la "
      "media; cuanto mayor es, más heterogéneo es el grupo.")
print()

# =====================================================================
print("Solución del ejercicio 7")
# =====================================================================
# Desviación estándar: raíz cuadrada de la varianza
desviacion_estandar_bucle = varianza_bucle ** 0.5

desviacion_estandar_funciones = math.sqrt(
    sum(map(lambda x: (x - media) ** 2, puntos)) / len(puntos)
)

desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)

print("desviacion_estandar_bucle:", desviacion_estandar_bucle)
print("desviacion_estandar_funciones:", desviacion_estandar_funciones)
print("desviacion_estandar_pandas:", desviacion_estandar_pandas)
print("¿Coinciden?", coinciden(desviacion_estandar_bucle,
                               desviacion_estandar_funciones,
                               desviacion_estandar_pandas))
print("Explicación: la desviación estándar está en las mismas unidades que los "
      "datos (puntos), mientras que la varianza está en puntos al cuadrado, "
      "por eso es más fácil de interpretar.")
print()

desviacion = desviacion_estandar_bucle

# =====================================================================
print("Solución del ejercicio 8")
# =====================================================================
# Normalización min-max: (valor - mínimo) / (máximo - mínimo)
minimo = min(puntos)
maximo = max(puntos)
print("Mínimo:", minimo, "| Máximo:", maximo)

normalizados_bucle = []
for punto in puntos:
    normalizados_bucle.append((punto - minimo) / (maximo - minimo))

normalizados_funciones = list(
    map(lambda x: (x - min(puntos)) / (max(puntos) - min(puntos)), puntos)
)

df["puntos_normalizados"] = (
    (df["puntos_prueba"] - df["puntos_prueba"].min())
    / (df["puntos_prueba"].max() - df["puntos_prueba"].min())
)
normalizados_pandas = list(df["puntos_normalizados"])

print("Método 1:", normalizados_bucle)
print("Método 2:", normalizados_funciones)
print("Método 3:", normalizados_pandas)
print("¿Coinciden?", coinciden(normalizados_bucle, normalizados_funciones,
                               normalizados_pandas))
print("Explicación: 0 es la nota mínima, 1 la máxima y 0.5 está justo a mitad "
      "de camino entre ambas.")
print()

# =====================================================================
print("Solución del ejercicio 9")
# =====================================================================
# Estandarización z-score: (valor - media) / desviación estándar
print("Media:", media, "| Desviación estándar:", desviacion)

z_bucle = []
for punto in puntos:
    z_bucle.append((punto - media) / desviacion)

z_funciones = list(map(lambda x: (x - media) / desviacion, puntos))

df["puntos_estandarizados"] = (
    (df["puntos_prueba"] - df["puntos_prueba"].mean())
    / df["puntos_prueba"].std(ddof=0)
)
z_pandas = list(df["puntos_estandarizados"])

print("Método 1:", z_bucle)
print("Método 2:", z_funciones)
print("Método 3:", z_pandas)
print("¿Coinciden?", coinciden(z_bucle, z_funciones, z_pandas))
print("Explicación: z positivo = por encima de la media; z negativo = por "
      "debajo; z cercano a 0 = muy próximo a la media. Indica cuántas "
      "desviaciones estándar se aleja el valor de la media.")
print()

# =====================================================================
print("Solución del ejercicio 10")
# =====================================================================
nombres = list(df["nombre"])

# Alumnos por encima de la media
encima_bucle = []
for i in range(len(puntos)):
    if puntos[i] > media:
        encima_bucle.append(nombres[i])

encima_funciones = list(
    map(lambda t: t[0],
        filter(lambda t: t[1] > media, zip(nombres, puntos)))
)

encima_pandas = list(df[df["puntos_prueba"] > media]["nombre"])

print("Por encima de la media (bucle):", encima_bucle)
print("Por encima de la media (filter):", encima_funciones)
print("Por encima de la media (pandas):", encima_pandas)
print("¿Coinciden?", encima_bucle == encima_funciones == encima_pandas)

# Alumnos por debajo de la media
debajo_bucle = []
for i in range(len(puntos)):
    if puntos[i] < media:
        debajo_bucle.append(nombres[i])

debajo_funciones = list(
    map(lambda t: t[0],
        filter(lambda t: t[1] < media, zip(nombres, puntos)))
)

debajo_pandas = list(df[df["puntos_prueba"] < media]["nombre"])

print("Por debajo de la media (bucle):", debajo_bucle)
print("Por debajo de la media (filter):", debajo_funciones)
print("Por debajo de la media (pandas):", debajo_pandas)
print("¿Coinciden?", debajo_bucle == debajo_funciones == debajo_pandas)

# Valor normalizado más alto y más bajo
max_norm = df["puntos_normalizados"].max()
min_norm = df["puntos_normalizados"].min()
print("Normalizado más alto (", max_norm, "):",
      list(df[df["puntos_normalizados"] == max_norm]["nombre"]))
print("Normalizado más bajo (", min_norm, "):",
      list(df[df["puntos_normalizados"] == min_norm]["nombre"]))

# Valores alejados del resto (criterio: |z| > 2)
atipicos = list(df[df["puntos_estandarizados"].abs() > 2]["nombre"])
if atipicos:
    print("Valores especialmente alejados del resto:", atipicos)
else:
    mas_lejano = df.loc[df["puntos_estandarizados"].abs().idxmax()]
    print("Ningún valor supera |z| > 2. El más alejado de la media es",
          mas_lejano["nombre"], "con z =", round(mas_lejano["puntos_estandarizados"], 3),
          "(no se considera un valor atípico).")

print("Conclusión: la media (74) es algo inferior a la mediana (75) y la moda es 80, "
      "así que el grupo rinde de forma aceptable, con la mayoría entre 60 y 90 puntos. "
      "La desviación estándar (~14.3) indica una dispersión moderada: Lucía (100) "
      "destaca por arriba y Ana (50) por abajo, pero sin casos extremos.")
