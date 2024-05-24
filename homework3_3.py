import csv
import re

# Имя исходного файла
input_filename = 'processed_prices.csv'
# Имя нового файла
output_filename = 'cleaned_prices.csv'


# Функция для обработки строки и извлечения первой суммы после названия
def extract_first_amount(row):
    # Регулярное выражение для поиска чисел, которые могут содержать пробелы
    number_pattern = re.compile(r'\d+\s*\d*')

    for item in row:
        match = number_pattern.search(item)
        if match:
            # Убираем лишние пробелы
            amount_str = match.group().replace(' ', '')
            try:
                amount = int(amount_str)
                return amount
            except ValueError:
                continue
    return None


# Открываем исходный файл для чтения и новый файл для записи
with open(input_filename, 'r', newline='', encoding='utf-8') as input_file, open(output_filename, 'w', newline='',
                                                                                 encoding='utf-8') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Записываем заголовок в новый файл
    writer.writerow(['Цена'])

    # Обрабатываем каждую строку и записываем в новый файл
    for row in reader:
        if len(row) > 1:
            amount = extract_first_amount(row[1:])
            if amount is not None:
                writer.writerow([amount])
