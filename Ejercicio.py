# -------------------------------
# ANALISIS DEL DATASET AMAZON BIG BILLION SALE 2025
# -------------------------------

import pandas as pd

# 1. Cargar el dataset
df = pd.read_csv(r"C:\Users\julio\Downloads\Amazon Big Billion Sale 2025 -Oct Mobile Phones.csv")

# 2. Resumen estadístico
print("🔹 Resumen estadístico del dataset:")
print(df.describe(include="all"))

# 3. Tipos de datos
print("\n🔹 Tipos de datos de cada columna:")
print(df.dtypes)

# 4. Primeros y últimos registros
print("\n🔹 Primeros registros del dataset:")
print(df.head())

print("\n🔹 Últimos registros del dataset:")
print(df.tail())

# 5. Ordenar resultados por precio (Top 10 más caros)
print("\n🔹 Top 10 productos más caros:")
print(df.sort_values(by="Price", ascending=False).head(10))

# 6. Medidas estadísticas de la columna "Price"
mean_price = df["Price"].mean()
median_price = df["Price"].median()
std_price = df["Price"].std()

print("\n🔹 Medidas estadísticas de la columna 'Price':")
print(f"Media: {mean_price:.2f}")
print(f"Mediana: {median_price:.2f}")
print(f"Desviación estándar: {std_price:.2f}")
