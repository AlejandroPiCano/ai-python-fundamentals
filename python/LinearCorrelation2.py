import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# We create two-variable data
np.random.seed(0)
x = np.random.randint(0, 10, 50)
y = np.random.randint(0, 10, 50)

# We create a function that represents the relationship between the variables
def modelo(x, a, b, c):
    return a * np.exp(b * x) + c

# We fit the model to the data
params, covariance = curve_fit(modelo, x, y)

# We create a line that fits the data
line = modelo(x, params[0], params[1], params[2])

# We create the scatter plotgit a
plt.scatter(x, y)
plt.plot(x, line, color='red')
plt.title('Regresión no Lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()