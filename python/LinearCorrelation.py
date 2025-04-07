import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create data
np.random.seed(0)
x = np.random.randint(0, 10, 50)
y = np.random.randint(0, 10, 50)

# Create the Linear Regression model
regression = LinearRegression()


# Training the regresion lineal model with the data
regression.fit(x.reshape(-1, 1), y)

# Create a straight line that fits the data
line = regression.coef_ * x + regression.intercept_

# Create the scatter plot
plt.scatter(x, y)
plt.plot(x, line, color='red')
plt.title('Regresión Lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()