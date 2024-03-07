import json
phone_book = []
with open('phonebook.txt', 'r', encoding='utf-8') as phin:
    for line in phin:
        values = line.strip().split(',')
        contact = {
            "last_name": values[0],
            "name": values[1],
            "number": values[2],
            "description": values[3]
        }
        phone_book.append(contact)

def work_with_phonebook():


    choice =show_menu()

    phone_book = read_txt('phonebook.txt')

    while (choice != 7):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book ,last_name))
        elif choice == 3:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            phone_book = 'phonebook.json'
            user_data = {
                "last_name": input(),
                "name": input(),
                "number": int(input()),
                "description": input()
            }
            add_person_to_phonebook(phone_book, user_data)
            print("Новый человек добавлен в телефонный справочник.")
        elif choice == 5:
            phone_book = 'phonebook.json'
            txt_file = 'phonebook.txt'
            save_phonebook_to_txt(phone_book, txt_file)
            print("Данные успешно сохранены в txt файл.")
        elif choice == 6:
            work_is_over()


        choice = show_menu()









def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input())
    return choice

def print_result(phone_book):
    with open(phone_book, 'r') as file:
        data = json.load(file)

    for index, contact in enumerate(data, start=1):
        print(f"Контакт {index}:")
        print("Фамилия:", contact['last_name'])
        print("Имя:", contact['name'])
        print("Номер телефона:", contact['phone_number'])
        print("Описание:", contact['description'])
        print()



def find_by_lastname(phone_book, last_name):
        with open(phone_book, 'r') as file:
            data = json.load(file)
        found_people = [person for person in data if person.get('last_name') == last_name]
        return found_people

def find_by_number(phone_book, number):
    with open(phone_book, 'r') as file:
        data = json.load(file)
    found_people = [person for person in data if person.get('phone_number') == number]
    return found_people

def add_person_to_phonebook(phone_book, user_data):
    with open(phone_book, 'r') as file:
        data = json.load(file)
    data.append(user_data)
    with open(phone_book, 'w') as file:
        json.dump(data, file, indent=4)

def save_phonebook_to_txt(phone_book, txt_file):
    with open(phone_book, 'r') as file:
        data = json.load(file)
    with open(txt_file, 'w') as file:
        for person in data:
            file.write(f"Фамилия: {person['last_name']}\n")
            file.write(f"Имя: {person['name']}\n")
            file.write(f"Номер телефона: {person['number']}\n")
            file.write(f"Описание: {person['description']}\n")
            file.write("\n")


def work_is_over():
    print("Работа с телефонной книгой завершена. До новых встреч!")

def read_txt(filename):

    phone_book =[]

    fields =['Фамилия', 'Имя', 'Телефон', 'Описание']



    with open(filename ,'r' ,encoding='utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(',')))

        # dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))

        phone_book.append(record)

    return phone_book








def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for contact in phone_book:
            contact_values = list(contact.values())
            line = ','.join(str(value) for value in contact_values)
            phout.write(f'{line}\n')















work_with_phonebook()


























