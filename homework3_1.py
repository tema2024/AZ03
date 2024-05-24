from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализация драйвера
driver = webdriver.Chrome()

url = 'https://www.divan.ru/category/divany-i-kresla'

driver.get(url)

# Задержка для загрузки страницы
time.sleep(5)

# Сбор данных
products = driver.find_elements(By.CLASS_NAME, 'WdR1o')

# Запись данных в CSV файл
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена'])

    for product in products:
        try:
            title = product.find_element(By.CLASS_NAME, 'lsooF').text
            price = product.find_element(By.CLASS_NAME, 'KIkOH').text
            writer.writerow([title, price])
        except Exception as e:
            print(f'Ошибка при обработке элемента: {e}')

# Закрытие браузера
driver.quit()







