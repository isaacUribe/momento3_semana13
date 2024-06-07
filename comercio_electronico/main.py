import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

productos_data = {
    'producto_id': [1, 2, 3, 4, 5],
    'nombre_producto': ['Camiseta', 'Pantalones', 'Laptop', 'Auriculares', 'Cafetera'],
    'categoria': ['Ropa', 'Ropa', 'Electrónica', 'Electrónica', 'Hogar'],
    'precio': [20.00, 35.00, 1000.00, 50.00, 80.00],
    'visitas': [150, 100, 300, 200, 120]
}
usuarios_data = {
    'usuario_id': [1, 2, 3, 4, 5],
    'nombre_usuario': ['Juan Perez', 'Ana Gomez', 'Carlos Ruiz', 'Laura Martinez', 'David Lopez'],
    'email': ['juan@example.com', 'ana@example.com', 'carlos@example.com', 'laura@example.com', 'david@example.com'],
    'edad': [28, 34, 22, 45, 30],
    'genero': ['M', 'F', 'M', 'F', 'M']
}
transacciones_data = {
    'transaccion_id': [1, 2, 3, 4, 5],
    'producto_id': [1, 3, 2, 5, 4],
    'usuario_id': [1, 2, 3, 4, 5],
    'fecha': ['2023-05-01 10:00:00', '2023-05-03 15:30:00', '2023-05-05 12:20:00', '2023-05-10 09:10:00', '2023-05-12 14:50:00'],
    'cantidad': [2, 1, 3, 1, 4]
}
resenas_data = {
    'reseña_id': [1, 2, 3, 4, 5],
    'transaccion_id': [1, 2, 3, 4, 5],
    'calificacion': [4, 5, 3, 4, 2],
    'comentario': ['Buena calidad.', 'Excelente producto.', 'Cumple su función.', 'Buen precio.', 'No funciona como esperaba.']
}

productos_df = pd.DataFrame(productos_data)
usuarios_df = pd.DataFrame(usuarios_data)
transacciones_df = pd.DataFrame(transacciones_data)
resenas_df = pd.DataFrame(resenas_data)

transacciones_completas_df = transacciones_df.merge(productos_df, on='producto_id', how='left')
transacciones_completas_df = transacciones_completas_df.merge(usuarios_df, on='usuario_id', how='left')
transacciones_completas_df = transacciones_completas_df.merge(resenas_df, on='transaccion_id', how='left')

transacciones_por_categoria = transacciones_completas_df.groupby('categoria')['transaccion_id'].nunique().reset_index(name='transacciones')
visitas_por_categoria = productos_df.groupby('categoria')['visitas'].sum().reset_index(name='visitas')
conversion_df = transacciones_por_categoria.merge(visitas_por_categoria, on='categoria')
conversion_df['tasa_conversion'] = conversion_df['transacciones'] / conversion_df['visitas']

plt.figure(figsize=(12, 6))
sns.barplot(data=conversion_df, x='categoria', y='tasa_conversion', palette='viridis')
plt.title('Tasa de Conversión por Categoría de Producto')
plt.xlabel('Categoría de Producto')
plt.ylabel('Tasa de Conversión')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

