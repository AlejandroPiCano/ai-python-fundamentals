import pandas as pd
import matplotlib.pyplot as plt

# Crear datos de ejemplo
data = {'Fecha': pd.date_range(start='1/1/2020', periods=365),
'Valor': pd.Series(range(1, 366))}

# Convertir datos a DataFrame de Pandas
df = pd.DataFrame(data)
df.set_index('Fecha', inplace=True)

# Aplicar transformación logarítmica
df['Valor_log'] = df['Valor'].apply(lambda x: np.log(x))

# Aplicar diferencia de primer orden
df['Diferencia_1'] = df['Valor'].diff(periods=1)

# Aplicar diferencia estacional
df['Diferencia_estacional'] = df['Valor'].diff(periods=365)

# Graficar las transformaciones
plt.plot(df['Valor'], label='Original')
plt.plot(df['Valor_log'], label='Logarítmica')
plt.plot(df['Diferencia_1'], label='Diferencia 1')
plt.plot(df['Diferencia_estacional'], label='Diferencia estacional')
plt.legend()
plt.show()