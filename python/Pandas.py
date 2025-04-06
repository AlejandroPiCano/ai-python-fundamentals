import pandas as pd

data = {
'ID': [1, 2, 3, 4, 5],
'Edad': [20, 25, 30, 35, 40],
'Altura': [160, 170, 180, 190, 200],
'Peso': [60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# summary using describe() function
summary = df.describe()


print(summary)