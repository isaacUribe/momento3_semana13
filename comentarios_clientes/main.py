import pandas as pd
from transformers import pipeline

df = pd.read_csv('comentatios.csv', sep=',')

sentiment_pipeline = pipeline('sentiment-analysis')

df['Sentimiento'] = df['Comentario'].apply(lambda comentario: sentiment_pipeline(comentario)[0]['label'])

print(df)