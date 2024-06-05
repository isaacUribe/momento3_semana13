import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

num_samples = 24 * 30
np.random.seed(0)

fechas = pd.date_range(start="2024-01-01", periods=num_samples, freq='h')
ubicaciones = ["Ubicacion 1", "Ubicacion 2", "Ubicacion 3"]
temperatura = np.random.uniform(15, 25, num_samples)
humedad = np.random.uniform(30, 70, num_samples)
calidad_aire = np.random.uniform(0, 100, num_samples)
ubicacion = np.random.choice(ubicaciones, num_samples)

data = {
    "FechaHora": fechas,
    "Ubicacion": ubicacion,
    "Temperatura": temperatura,
    "Humedad": humedad,
    "Calidad Aire": calidad_aire
}

df = pd.DataFrame(data)

df["FechaHora"] = pd.to_datetime(df["FechaHora"])

columas_numericas = ['FechaHora','Temperatura', 'Humedad', 'Calidad Aire']
df_numericas = df[columas_numericas]

df_diario = df_numericas.resample('D', on='FechaHora').mean()

print(df_diario)

plt.figure(figsize=(10, 6))
plt.plot(df_diario.index, df_diario['Temperatura'], label="Temperatura")
plt.xlabel('Fecha')
plt.ylabel('Temperatura')
plt.title('Temperatura')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df_diario.index, df_diario['Humedad'], label="Humedad")
plt.xlabel('Fecha')
plt.ylabel('Humedad')
plt.title('Humedad')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df_diario.index, df_diario['Calidad Aire'], label="Calidad Aire")
plt.xlabel('Fecha')
plt.ylabel('Calidad Aire')
plt.title('Calidad Aire')
plt.legend()
plt.grid(True)
plt.show()

correlacion = df_diario.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Heatmap Correlacion")
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x=df_diario['Temperatura'], y=df_diario['Humedad'], line_kws={"color":"red"})
plt.xlabel('Temperatura')
plt.ylabel('Humedad')
plt.title("Relacion entre Temperatura y humedad")
plt.grid(True)
plt.show()

#print(df)