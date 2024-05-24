import numpy as np
import matplotlib.pyplot as plt

num_samples = 100
x_data = np.random.rand(num_samples)
y_data = np.random.rand(num_samples)

plt.scatter(x_data, y_data, alpha=0.6, edgecolors='w', s=50)
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X данные')
plt.ylabel('Y данные')
plt.grid(True)
plt.show()
