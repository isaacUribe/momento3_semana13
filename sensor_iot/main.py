import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

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
#print(df)