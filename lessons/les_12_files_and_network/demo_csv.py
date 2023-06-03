"""
CSV (от англ. Comma-Separated Values — значения, разделённые запятыми) - формат хранения данных


demo_ используется для избегания коллизий в пространстве имён

json хорош
"""

import csv

FILENAME = 'cars.csv'
USERS_FILE = 'users.csv'


def demo_read_csv():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for not_first, row in enumerate(reader):
            if not_first:  # 0 == False
                print(row[1], row[2], row[0])
            else:
                print('heads:', row)


def demo_read_csv_dict():
    with open(FILENAME, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        print('headers:', csv_reader.fieldnames)
        for row in csv_reader:
            print(row)
            print(row['Make'], row['Model'], row['Year'])


class FieldNames:
    USERNAME = 'username'
    EMAIL = 'email'
    RED_DATE = 'data reg'


def write_csv():
    fieldnames = [
        FieldNames.USERNAME,
        FieldNames.EMAIL,
        FieldNames.RED_DATE,
    ]
    with open(USERS_FILE, 'w') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        user_info = {
            FieldNames.USERNAME: 'Ben',
            FieldNames.EMAIL: 'Ben@m.ru',
            FieldNames.RED_DATE: '2023-06-06',
        }

        users_info = [{
            FieldNames.USERNAME: 'Sam',
            FieldNames.EMAIL: 'Ben@m.ru',
            FieldNames.RED_DATE: '2023-06-06',
        },
        {
            FieldNames.USERNAME: 'Jim',
            FieldNames.EMAIL: 'Ben@m.ru',
            FieldNames.RED_DATE: '2023-06-06',
        }]

        # Записываем данные в файл
        csv_writer.writerow(user_info)
        csv_writer.writerows(users_info)


def main():
    # demo_read_csv()
    # demo_read_csv_dict()
    write_csv()


if __name__ == "__main__":
    main()


