# LuisOR
import csv
import os

FILE_NAME = 'businesses.csv'
HEADERS = ['ruc', 'business_name', 'direction']

def load_data():
    collection = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8', newline='') as file:
            readercvs = csv.DictReader(file)
            for item in readercvs:
                collection[item[HEADERS[0]]] = {f'{HEADERS[1]}':item[f'{HEADERS[1]}'], f'{HEADERS[2]}':item[f'{HEADERS[2]}']}
    return collection

def save_data(collection):
    with open(FILE_NAME, 'w', encoding='utf-8', newline='') as file:
        writercsv = csv.DictWriter(file, fieldnames=HEADERS)
        writercsv.writeheader()
        for index, item in collection.items():
            writercsv.writerow({f'{HEADERS[0]}':index, f'{HEADERS[1]}':item[f'{HEADERS[1]}'], f'{HEADERS[2]}': item[f'{HEADERS[2]}']})

businesses = load_data()