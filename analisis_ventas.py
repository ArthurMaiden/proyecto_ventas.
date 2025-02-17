import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos correctamente asegurando que usa la coma como separador
df = pd.read_csv('ventas_productos.csv', sep=",", encoding="utf-8")

# Depuración: Mostrar qué columnas se cargaron realmente
print("Columnas cargadas en el DataFrame:", df.columns)

# Intentar limpiar espacios en nombres de columnas
df.columns = df.columns.str.strip()

# Calcular el precio total por producto
df['Precio_Total'] = df['Cantidad'] * df['Precio']

# Mostrar los primeros registros
print(df.head())

# Crear un gráfico de barras para visualizar el precio total por producto
plt.bar(df['Producto'], df['Precio_Total'], color='skyblue')

# Etiquetas y título del gráfico
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')

# Guardar el gráfico como PNG
plt.savefig('grafico_precios.png')

# Mostrar el gráfico
plt.show()
