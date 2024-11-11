import csv
import json
import os

#Функція для створення та запису даних у CSV файл
def create_csv_file(file_path):
    data = [
        {"id": 1, "name": "Давид", "age": 19, "grade": "90"},
        {"id": 2, "name": "Вася", "age": 18, "grade": "100"},
        {"id": 3, "name": "Поліна", "age": 20, "grade": "67"},
    ]

    #Обробка виключних ситуацій при роботі з файлом
    try:
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            print(f"CSV файл '{file_path}' успішно створений.")
    except IOError as e:
        print(f"Помилка при записі у файл: {e}")

#Функція для конвертації CSV файлу у JSON
def csv_to_json(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

            with open(json_file_path, mode='w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"CSV файл '{csv_file_path}' успішно конвертований у JSON файл '{json_file_path}'.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except IOError as e:
        print(f"Помилка при обробці файлу: {e}")

#Шлях до файлів
csv_file_path = 'students.csv'
json_file_path = 'students.json'

#Виклик функцій
create_csv_file(csv_file_path)
csv_to_json(csv_file_path, json_file_path)
