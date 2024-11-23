#Марюха Дар'я
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
        
# Функція додавання нових данних в JSON файл
def append_to_json_file(json_file_path, new_data):
    try:
        #Читання існуючих даних
        with open(json_file_path, mode='r') as json_file:
            data = json.load(json_file)
        #Додавання нових записів
        data.extend(new_data)
        # Записування нових данних в JSON файл
        with open(json_file_path, mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Новые данные успешно добавлены в JSON файл '{json_file_path}'.")
    except FileNotFoundError:
        print("JSON файл не найден.")
    except IOError as e:
        print(f"Ошибка при обновлении JSON файла: {e}")

# Функція переписування даних з файлу JSON в файл CSV
def json_to_csv(json_file_path, csv_file_path):
    try:
        # Зчитування данних з JSON файлу
        with open(json_file_path, mode='r') as json_file:
            data = json.load(json_file)
        # Записування даних в CSV файл
        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            print(f"JSON файл '{json_file_path}' успешно переписан в CSV файл '{csv_file_path}'.")
    except FileNotFoundError:
        print("JSON файл не найден.")
    except IOError as e:
        print(f"Ошибка при записи в CSV файл: {e}")
        
#Шлях до файлів
csv_file_path = 'students.csv'
json_file_path = 'students.json'

#Виклик функцій
create_csv_file(csv_file_path)
csv_to_json(csv_file_path, json_file_path)
append_to_json_file(json_file_path, new_data)
json_to_csv(json_file_path, csv_file_path)


#Половинка Софія
# Функція для додавання даних з CSV у JSON без дублювання
def csv_to_json_unique_append(csv_file_path, json_file_path, new_data):
    try:
        # Зчитування даних із CSV-файлу
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            csv_data = [row for row in csv_reader]

        # Зчитування існуючого JSON-файлу
        with open(json_file_path, mode='r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        # Перетворення JSON-даних у словник для швидкого пошуку за id
        existing_ids = {int(student['id']) for student in json_data}

        # Додавання записів із CSV, якщо їх id ще немає у JSON
        for row in csv_data:
            if int(row['id']) not in existing_ids:
                json_data.append(row)
                existing_ids.add(int(row['id']))

        # Додавання нових даних
        for student in new_data:
            if int(student['id']) not in existing_ids:
                json_data.append(student)
                existing_ids.add(int(student['id']))

        # Перезапис JSON-файлу з унікальними записами
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        print(f"Дані з '{csv_file_path}' успішно додані до JSON-файлу '{json_file_path}' без повторень.")
    except FileNotFoundError:
        print("CSV або JSON файл не знайдено.")
    except IOError as e:
        print(f"Помилка при обробці файлу: {e}")

# Нові дані для додавання
new_data = [
    {"id": 6, "name": "Марія", "age": 23, "grade": "78"},
    {"id": 7, "name": "Іван", "age": 24, "grade": "82"}
]

# Шляхи до файлів
csv_file_path = 'students.csv'
json_file_path = 'students.json'

# Виклик функції
csv_to_json_unique_append(csv_file_path, json_file_path, new_data)
