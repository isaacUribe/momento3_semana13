import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Nombre Usuario": ["Juan", "Juan", "Jose", "Maria", "Juanita", "Jose", "Maria", "David", "Josefa"],
    "Cantidad": [10, 20, 12, 50, 30, 24, 15, 47, 50],
    "Fecha": ["12-05-2024", "15-05-2024", "10-05-2024", "20-05-2024", "05-05-2024", "13-05-2024", "30-05-2024", "10-05-2024", "25-05-2024"],
    "Tipo Transaccion": ["Deposito", "Retiro", "Deposito", "Retiro", "Deposito", "Retiro", "Deposito", "Retiro", "Deposito"],
    "Saldo Final": [410, 390, 412, 365, 430, 500, 200, 460, 140]
}

df = pd.DataFrame(data)

df["Fecha"] = pd.to_datetime(df["Fecha"], format='%d-%m-%Y')

df = df.sort_values(by=["Nombre Usuario","Fecha"])

df["Saldo Diario"] = df.groupby("Nombre Usuario")["Saldo Final"].diff().fillna(df["Saldo Final"])

promedio_saldo_diario = df.groupby("Nombre Usuario")["Saldo Diario"].mean().reset_index()

promedio_saldo_diario.columns = ["Nombre Usuario", "Promedio Saldo Diario"]

retiros = df[df["Tipo Transaccion"] == "Retiro"]

cantidad_total_retiros = retiros.groupby("Nombre Usuario")["Cantidad"].sum().reset_index()

cantidad_total_retiros.columns = ["Nombre Usuario", "Cantidad Retiros"]

depositos = df[df["Tipo Transaccion"] == "Deposito"]

cantidad_total_deposito = depositos.groupby("Nombre Usuario")["Cantidad"].sum().reset_index()

cantidad_total_deposito.columns = ["Nombre Usuario", "Cantidad Depositos"]

print(promedio_saldo_diario)

print(cantidad_total_retiros)
print(cantidad_total_deposito)

print(df)

df_saldo_promedio = df.groupby(["Nombre Usuario", "Fecha"])["Saldo Diario"].mean().reset_index()
transacciones_por_usuario = df["Nombre Usuario"].value_counts().head(5).index

df_top_usuarios = df_saldo_promedio[df_saldo_promedio["Nombre Usuario"].isin(transacciones_por_usuario)]



plt.figure(figsize=(10, 6))

for usuario in transacciones_por_usuario:
    df_usuario = df_top_usuarios[df_top_usuarios["Nombre Usuario"] == usuario]
    plt.plot(df_usuario["Fecha"], df_usuario["Saldo Diario"], label=usuario)

# Añadir etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Saldo Promedio Diario')
plt.title('Evolución del Saldo Promedio Diario para los 5 Usuarios con Más Transacciones')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()


top_usuarios = df["Nombre Usuario"].value_counts().head(5).index

df_top_usuarios = df[df["Nombre Usuario"].isin(top_usuarios)]

total_transacciones = df_top_usuarios.groupby(["Nombre Usuario", "Tipo Transaccion"])["Cantidad"].sum().unstack(fill_value=0).reset_index()

total_transacciones.plot(kind="bar", x="Nombre Usuario", stacked=True)

# Añadir etiquetas y título
plt.xlabel('Nombre Usuario')
plt.ylabel('Cantidad Total')
plt.title('Comparación del Total de Depósitos y Retiros para los 5 Usuarios con Más Transacciones')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()