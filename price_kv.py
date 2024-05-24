import csv

def clean_price(price):
    return int(price.replace(' ₽/мес.', '').replace(' ', ''))

input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            clean_row = [clean_price(row[0])]
            writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")
