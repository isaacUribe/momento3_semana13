import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = {
    'Usuario': ['user1', 'user2', 'user1', 'user3', 'user2', 'user1', 'user3', 'user2', 'user4', 'user5', 'user4', 'user5', 'user4', 'user6', 'user7', 'user8', 'user9', 'user10', 'user6', 'user7'],
    'Fecha': [
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
        '2024-02-01', '2024-02-03', '2024-02-04', '2024-02-05', '2024-02-06',
        '2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05',
        '2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05'
    ],
    'Texto': [
        '¡Feliz Año Nuevo a todos!', 'Me encanta este lugar', 'Nuevo post en el blog, ¡échale un vistazo!',
        'El clima está increíble hoy', 'Pasando un buen rato con amigos', 'Iniciando el mes con nuevas metas',
        'Tarde de relajación en el parque', 'Evento en vivo esta noche, no te lo pierdas!',
        'Deliciosa comida en el restaurante', 'Explorando nuevos lugares', 'Noche de películas con amigos',
        'Disfrutando el día en la playa', 'Paseo por la ciudad', 'Nueva receta en el blog', 'Día de compras',
        'Entrenamiento en el gimnasio', 'Visita a la familia', 'Leyendo un buen libro', 'Fin de semana en el campo', 'Preparando un nuevo proyecto'
    ],
    'Me Gusta': [100, 150, 200, 50, 80, 300, 120, 130, 140, 160, 110, 90, 70, 130, 170, 180, 110, 95, 210, 205],
    'Compartidos': [10, 20, 30, 5, 8, 50, 12, 15, 18, 22, 11, 9, 7, 13, 17, 18, 11, 10, 21, 20]
}

df = pd.DataFrame(data)

df['Fecha'] = pd.to_datetime(df['Fecha'])

df['Longitud Texto'] = df['Texto'].apply(len)

df_agrupado = df.groupby('Usuario').agg({
    'Me Gusta': 'mean',
    'Compartidos': 'mean',
    'Longitud Texto': 'mean'
}).reset_index()

print(df)

plt.figure(figsize=(10, 6))
plt.scatter(df['Longitud Texto'], df['Me Gusta'], c='blue', alpha=0.5)
plt.title('Relación entre la Longitud del Texto y el Número de Me Gusta')
plt.xlabel('Longitud del Texto')
plt.ylabel('Número de Me Gusta')
plt.grid(True)
plt.show()

df_agrupado = df.groupby('Usuario').agg({
    'Me Gusta': 'mean',
    'Compartidos': 'mean',
    'Longitud Texto': 'mean',
    'Fecha': 'count'
}).rename(columns={'Fecha': 'Publicaciones'}).reset_index()

df_top_usuarios = df_agrupado.sort_values(by='Publicaciones', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.35
index = df_top_usuarios['Usuario']

bar1 = ax.bar(index, df_top_usuarios['Me Gusta'], bar_width, label='Promedio de Me Gusta')
bar2 = ax.bar(index, df_top_usuarios['Compartidos'], bar_width, bottom=df_top_usuarios['Me Gusta'], label='Promedio de Compartidos')

ax.set_xlabel('Usuario')
ax.set_ylabel('Promedio')
ax.set_title('Promedio de Me Gusta y Compartidos por Usuario (Top 10 Usuarios Más Activos)')
ax.set_xticks(index)
ax.set_xticklabels(index, rotation=45)
ax.legend()

plt.show()


plt.figure(figsize=(12, 8))
sns.violinplot(x='Longitud Texto', y='Me Gusta', data=df)
plt.xlabel('Longitud del Texto de la Publicación')
plt.ylabel('Número de Me Gusta')
plt.title('Distribución del Número de Me Gusta por Longitud del Texto de la Publicación')
plt.show()



