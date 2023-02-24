contacts_file = r'Homework_8\contacts.txt'

def append_contact(contacts_file):
    contact = input('Введите контакт в формате: ФИО -> Телефон: ')
    with open(contacts_file, 'a', encoding='utf-8') as f:
        f.write(f'\n{contact}')
    print('Контакт добавлен')

def read_contact(contacts_file):
    with open(contacts_file, 'r', encoding='utf-8') as f:
        print(f.read())

def search_contact(contacts_file):
    search_by = input('Введите информацию для поиска: ')
    with open(contacts_file, 'r', encoding='utf-8') as f:
        for line in f:
            if search_by in line:
                print(line)
                
def delete_contact(contacts_file):
    deletion = input('Введите контакт для удаления: ')
    with open(contacts_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(contacts_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if deletion in line:
                del line
                continue
            f.write(line)
                
def change_contact(contacts_file):
    change_line = input('Какой контакт вы хотите изменить?\n')
    with open(contacts_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(contacts_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if change_line in line:
                f.write(input('Введите данные нового контакта в формате: ФИО -> Телефон\n'))
                f.write('\n')
                continue
            f.write(line)
            
def user_action():
    print('Добро пожаловать!\n \
         1) Вывести весь справочник\n \
         2) Добавить контакт\n \
         3) Найти контакт\n \
         4) Удалить контакт\n \
         5) Изменить контакт')
    while (user_input := int(input('Выберите действие со справочником(0 = выход): '))) != 0:
        if user_input == 1:
            read_contact(contacts_file)
        elif user_input == 2:
            append_contact(contacts_file)
        elif user_input == 3:
            search_contact(contacts_file)
        elif user_input == 4:
            delete_contact(contacts_file)
        elif user_input == 5:
            change_contact(contacts_file)
        else:
            print('Некорректный ввод')
            
user_action()