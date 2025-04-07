import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv("titanic.csv")

# Mostrar primeras filas del dataset
print(titanic.head())

# Distribución de edades
plt.figure(figsize=(10, 6))
sns.histplot(data=titanic, x="age", kde=True, bins=30, color='skyblue')
plt.title("Distribución de Edades de los Pasajeros del Titanic")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# Pasajeros por clase
plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x="pclass", palette="muted")
plt.title("Cantidad de Pasajeros por Clase de Boleto")
plt.xlabel("Clase")
plt.ylabel("Cantidad de Pasajeros")
plt.xticks(ticks=[0, 1, 2], labels=["Primera", "Segunda", "Tercera"])
plt.show()

# Proporción de sobrevivientes por sexo
survival_sex = titanic.groupby("sex")["survived"].value_counts(normalize=True).unstack()
print("\nProporción de sobrevivientes por sexo (tabla):")
print(survival_sex)

survival_sex.plot(kind="bar", stacked=True, color=["salmon", "mediumseagreen"])
plt.title("Proporción de Sobrevivientes por Sexo")
plt.ylabel("Proporción")
plt.xlabel("Sexo")
plt.legend(["No sobrevivió", "Sobrevivió"], loc="upper right")
plt.xticks(rotation=0)
plt.show()
