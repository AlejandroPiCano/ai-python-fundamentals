import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
# Crear datos de ejemplo
data = {'Fecha': pd.date_range(start='1/1/2020', periods=365),'Valor': pd.Series(range(1, 366))}

# Convertir datos a DataFrame de Pandas
df = pd.DataFrame(data)
df.set_index('Fecha', inplace=True)

# Ajustar un modelo SARIMA
sarima_model = sm.tsa.statespace.SARIMAX(df['Valor'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_results = sarima_model.fit()

# Graficar la serie temporal y las predicciones
plt.plot(df['Valor'], label='Serie temporal original')
plt.plot(sarima_results.predict(start=1, end=365), label='Predicciones SARIMA')
plt.legend()
plt.show()