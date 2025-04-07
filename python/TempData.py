import pandas as pd
import matplotlib.pyplot as plt

# Crear datos de ejemplo
data = {'Fecha': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
'Valor': [10, 12, 8, 15, 13]}

# Convertir datos a DataFrame de Pandas
df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Configurar la fecha como índice
df.set_index('Fecha', inplace=True)

# Graficar datos
plt.plot(df.index, df['Valor'])
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.title('Análisis de series temporales')
plt.show()