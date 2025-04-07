import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
'Satisfacción': ['Excelente', 'Bueno', 'Regular', 'Malo', 'Excelente', 'Bueno', 'Regular', 'Malo'],
'Ingresos': ['Bajo', 'Medio', 'Medio', 'Alto', 'Medio', 'Medio', 'Bajo', 'Alto']
}
df = pd.DataFrame(data)

# Do a cross-variable analysis
cross_tab = pd.crosstab(df['Satisfacción'], df['Ingresos'])

# Show the results
cross_tab.plot(kind='bar', stacked=True)
plt.title('Cross-variable analysis: Satisfaction vs Incomes')
plt.xlabel('Satisfaction')
plt.ylabel('Customer Count')
plt.legend(title='Incomes')
plt.show()