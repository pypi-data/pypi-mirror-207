import sys
from hashlib import md5
from prettytable import PrettyTable

fields = {
    "phone": "Телефонный номер"
}

if __name__ == "__main__":

    if sys.argv.__len__() == 2:
        command = sys.argv[1]
        table = PrettyTable()
        table.field_names = ["Тип данных", "Обозначение"]
        table.add_rows([[key, value] for key, value in fields.items()])
        if command == "fields":
            print("Наименования полей, используемых в общем проекте:\n")
            print(table)
            print("\nАктуальная информация доступна по ссылке: nahuy.org")
    elif sys.argv.__len__() == 3:
        command = sys.argv[1]
        value = sys.argv[2]
        if command == "hash":
            try:
                print(md5(value.encode('utf-8')).hexdigest())
            except UnicodeDecodeError:
                print("Не удалось преобразовать значение")

