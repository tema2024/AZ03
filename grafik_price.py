import pandas as pd
import matplotlib.pyplot as plt

file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

prices = data['Price']

plt.hist(prices, bins=10, edgecolor='black')

plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()
