import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np


# ==========================================
# GENERACIÓN DEL DATASET 5 (VENTAS)
# ==========================================
random.seed(42)
n = 100
productos = ['Laptop Dell', 'iPhone 14', 'Samsung TV', 'iPad Pro', 'MacBook Air',
             'Monitor LG', 'Teclado Logitech', 'Mouse Microsoft', 'Auriculares Sony', 'Impresora HP']
categorias = ['Electrónica', 'Computación', 'Telefonía', 'Accesorios', 'Oficina']
vendedores = ['Carlos Ruiz', 'María López', 'Juan Pérez', 'Ana Martínez', 'Luis García']
regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
clientes_tipo = ['Individual', 'Empresa', 'Gobierno', 'Educación']
metodos_pago = ['Tarjeta', 'Transferencia', 'Efectivo', 'Crédito', 'PayPal']

fecha_inicio = datetime.now() - timedelta(days=365)
fechas = [fecha_inicio + timedelta(days=random.randint(0, 365)) for _ in range(n)]

df = pd.DataFrame({
    'id_venta': range(1, n+1),
    'fecha': [fecha.strftime('%Y-%m-%d') for fecha in fechas],
    'producto': [random.choice(productos) for _ in range(n)],
    'categoria': [random.choice(categorias) for _ in range(n)],
    'cantidad': [random.randint(1, 10) for _ in range(n)],
    'precio_unitario': [random.randint(100, 5000) for _ in range(n)],
    'costo': [random.randint(50, 3000) for _ in range(n)],
    'vendedor': [random.choice(vendedores) for _ in range(n)],
    'region': [random.choice(regiones) for _ in range(n)],
    'cliente_tipo': [random.choice(clientes_tipo) for _ in range(n)],
    'descuento': [round(random.uniform(0.0, 0.3), 2) for _ in range(n)],
    'metodo_pago': [random.choice(metodos_pago) for _ in range(n)]
})

# Creamos la columna necesaria para los siguientes puntos
df['ingreso_total'] = df['cantidad'] * df['precio_unitario']

# ==========================================
# RESOLUCIÓN DE LA EVALUACIÓN (PUNTOS 1 AL 20)
# ==========================================

# 1. Vista preliminar
print(df.head())

# 2. Información estructural
print(df.shape)
df.info()

# 3. Estadísticas descriptivas
print(df.describe())

# 4. Filtrado simple
print(df[df['cantidad'] > 5])

# 5. Selección con .loc
print(df.loc[0:4, ['producto', 'vendedor']])

# 6. Selección con .iloc
print(df.iloc[0:3, 2:4])

# 7. Métricas estadísticas individuales
print(df['precio_unitario'].mean())
print(df['cantidad'].max())
print(df['costo'].sum())

# 8. Nueva columna derivada
df['ingreso_total'] = df['cantidad'] * df['precio_unitario']

# 9. Ordenar datos y Top N
print(df.sort_values(by='ingreso_total', ascending=False).head(5))

# 10. Conteos por categoría
print(df['vendedor'].value_counts())

# 11. Agrupaciones con groupby y agregación
print(df.groupby('categoria').agg({'precio_unitario': ['mean', 'max'], 'cantidad': 'sum'}))

# 12. Agrupación múltiple
print(df.groupby(['region', 'categoria'])['ingreso_total'].mean())

# 13. Variable categórica con pd.cut y tabla cruzada
df['rango_precio'] = pd.cut(df['precio_unitario'], bins=[0, 1000, 3000, 5000], labels=['Bajo', 'Medio', 'Alto'])
