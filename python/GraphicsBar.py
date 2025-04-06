import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
frecuencies = [20, 30, 25, 35]

# Create histogram
plt.bar(categories, frecuencies, color='skyblue')

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.title('Graphics Bar')
# Show the graphics
plt.show()