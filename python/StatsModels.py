import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Crear datos de ejemplo
data = {'Fecha': pd.date_range(start='1/1/2020', periods=365),
'Valor': pd.Series(range(1, 366))}

# Convertir datos a DataFrame de Pandas
df = pd.DataFrame(data)
df.set_index('Fecha', inplace=True)

# Descomponer la serie temporal
decomposition = sm.tsa.seasonal_decompose(df['Valor'], model='additive')

# Graficar las componentes
plt.subplot(4, 1, 1)
plt.plot(decomposition.trend)
plt.title('Tendencia')
plt.subplot(4, 1, 2)
plt.plot(decomposition.seasonal)
plt.title('Estacionalidad')
plt.subplot(4, 1, 3)
plt.plot(decomposition.resid)
plt.title('Variación irregular')
plt.subplot(4, 1, 4)
plt.plot(df['Valor'])
plt.title('Serie original')
plt.tight_layout()
plt.show()