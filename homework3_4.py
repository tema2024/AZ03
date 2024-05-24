import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла
input_filename = 'cleaned_prices.csv'
data = pd.read_csv(input_filename)

# Вычисление средней цены
average_price = data['Цена'].mean()
print(f"Средняя цена: {average_price}")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(data['Цена'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
