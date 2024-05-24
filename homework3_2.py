import csv
import re

# Имя исходного файла
input_filename = 'prices.csv'
# Имя нового файла
output_filename = 'processed_prices.csv'


# Функция для обработки строки и извлечения первой суммы после названия
def extract_first_amount(row):
    # Регулярное выражение для поиска чисел, которые могут содержать пробелы
    number_pattern = re.compile(r'\d+\s*\d*')

    # Создаем новую строку, где будут только название и первая найденная цена
    new_row = [row[0]]

    for item in row[1:]:
        match = number_pattern.search(item)
        if match:
            # Убираем лишние пробелы
            amount_str = match.group().replace(' ', '')
            try:
                amount = int(amount_str)
                new_row.append(amount)
                break  # Прекращаем обработку после первой найденной суммы
            except ValueError:
                continue

    # Если не удалось найти цену, добавляем None
    if len(new_row) == 1:
        new_row.append(None)

    return new_row


# Открываем исходный файл для чтения и новый файл для записи
with open(input_filename, 'r', newline='', encoding='utf-8') as input_file, open(output_filename, 'w', newline='',
                                                                                 encoding='utf-8') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Пропускаем заголовок
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем каждую строку и записываем в новый файл
    for row in reader:
        # Обрабатываем строку, удаляя кавычки в начале и конце строки, а также разделяем по новой строке
        row = [x.strip() for x in row[0].split('\n') if x.strip()]
        processed_row = extract_first_amount(row)
        writer.writerow(processed_row)




