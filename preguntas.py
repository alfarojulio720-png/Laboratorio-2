#Matera Programacio 3
#Trabajo: Laboratorio 2
# Alumnos: Shelsy Melendez SMSS096724 y julio Alfaro SMSS216923

# 1-) Describe brevemente de qué trata el dataset utilizado
# Nuestra dataset es de una Gran Venta india de Amazon 22- 2025 - Teléfonos móviles

#2-) ¿Qué información permite ver el resumen estadístico?
#El resumen estadístico (describe(include="all")) proporciona:

#Para columnas numéricas (como Price):
#Media, mediana, mínimo, máximo, desviación estándar, percentiles.
#Para columnas categóricas (como Brand o Product Name):
#Frecuencia del valor más común (top), cuántas veces aparece (freq), número de valores únicos (unique), y valores faltantes.
#Esto permite identificar:
#Qué marcas tienen más modelos
#Rango y dispersión de precios
#Existencia de productos atípicos o fuera de rango

#3-) ¿Qué cambios o tendencias se detectan en la información del dataset?
#Aunque no se incluyen fechas explícitas en el código, con el análisis de los precios y las especificaciones podemos detectar tendencias como:
#Muchos dispositivos tienen precios reducidos debido a las ofertas del evento.
#Algunos productos muestran grandes descuentos, lo cual puede indicar estrategias agresivas para modelos específicos.
#Las marcas con mayor número de modelos o mayor presencia en los top de precios podrían estar dominando la campaña.

#4-)¿Qué categorías sobresalen en la comparación y por qué crees que será?
#Al comparar por precios o frecuencia, sobresalen:
#Marcas como Apple, Samsung o OnePlus, probablemente por su posicionamiento premium (por eso aparecen en el top de productos más caros).
#También podrían destacar marcas como Xiaomi o Realme en cantidad de modelos disponibles, debido a su gama media y asequible.
#Estas marcas destacan por:
#Fuerte presencia en el mercado
#Variedad de modelos para distintos presupuestos
#Reputación o campañas de marketing en eventos como el Big Billion Sale

#5-)¿Qué diferencias se observan entre los primeros y últimos registros?
#Según df.head() y df.tail(), puedes comparar:
#Marcas o precios diferentes
#Especificaciones o descuentos cambiantes
#Podría notarse que los primeros registros pertenecen a marcas más comunes o con menor precio, y los últimos a modelos de alta gama o menos comunes (aunque esto depende del orden del dataset original).

#6-) ¿Qué aportan las medidas estadísticas al análisis del dataset?
#Las medidas estadísticas como la media, mediana y desviación estándar del precio permiten:
#Entender el precio promedio de los móviles durante la venta.
#Ver si hay asimetría en los datos (por ejemplo, si la media es muy distinta de la mediana, hay outliers).
#Identificar la variabilidad de precios, lo que indica si hay una gran variedad de gamas (baja, media, alta).
#Estas métricas son fundamentales para:
#Toma de decisiones comerciales (qué gama de producto promover)
#Comparación entre marcas
#Detección de productos fuera de rango o con precios sospechosos