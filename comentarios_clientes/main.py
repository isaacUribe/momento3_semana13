import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('comentatios.csv', sep=',')

sentiment_pipeline = pipeline('sentiment-analysis')

df['Sentimiento'] = df['Comentario'].apply(lambda comentario: sentiment_pipeline(comentario)[0]['label'])

df['Fecha'] = pd.to_datetime(df['Fecha'])

df.set_index('Fecha', inplace=True)

df['Mes'] = df.index.to_period('M')

resultados = pd.DataFrame()

for sentimiento in ['POSITIVE', 'NEGATIVE', 'NEUTRAL']:
    df_sentimiento = df[df['Sentimiento'] == sentimiento].resample('M').size()
    resultados[sentimiento] = df_sentimiento 

resultados = resultados.fillna(0)


promedio_mensuales = resultados.mean()
print(promedio_mensuales)

print(df)

plt.figure(figsize=(10, 6))
plt.plot(resultados.index, resultados['POSITIVE'], label='Positivos', marker='o')
plt.plot(resultados.index, resultados['NEGATIVE'], label='Negativos', marker='o')
plt.plot(resultados.index, resultados['NEUTRAL'], label='Neutros', marker='o')

plt.title('Tendencias Sentimientos')
plt.xlabel('Mes')
plt.ylabel('Cantidad Comentarios')
plt.legend()
plt.grid(True)
plt.show()

calificaciones_altas = df[df['Calificacion'].isin([4, 5])]
calificaciones_bajas = df[df['Calificacion'].isin([1, 2])]

sentimientos_alta = calificaciones_altas['Sentimiento'].value_counts()
snetimientos_baja = calificaciones_bajas['Sentimiento'].value_counts()

resultados = pd.DataFrame({
    'Calificiacion Alta': sentimientos_alta,
    'Calificacion Baja': snetimientos_baja
}).fillna(0)

resultados.plot(kind='bar', figsize=(10, 6))
plt.title('Distribución de Sentimientos por Calificación de Producto')
plt.xlabel('Sentimiento')
plt.ylabel('Cantidad de Comentarios')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

comentarios_positivos = df[df['Sentimiento'] == 'POSITIVE']['Comentario']
comentarios_negativos = df[df['Sentimiento'] == 'NEGATIVE']['Comentario']

texto_positivo = ' '.join(comentarios_positivos)
wordcloud_positivo = WordCloud(width=800, height=400, background_color='white').generate(texto_positivo)

texto_negativo = ' '.join(comentarios_negativos)
wordcloud_negativo = WordCloud(width=800, height=400, background_color='white').generate(texto_negativo)

plt.figure(figsize=(14, 7))


plt.subplot(1, 2, 1)
plt.imshow(wordcloud_positivo, interpolation='bilinear')
plt.axis('off')
plt.title('Nube de Palabras - Comentarios Positivos')


plt.subplot(1, 2, 2)
plt.imshow(wordcloud_negativo, interpolation='bilinear')
plt.axis('off')
plt.title('Nube de Palabras - Comentarios Negativos')

plt.show()