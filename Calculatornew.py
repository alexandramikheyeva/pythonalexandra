
def print_valie_dict():
    print(dict.get(input('Print key(id): ')))

    dict = {0:{'id':'a',
                  'age':'12',
                  'name':'123',
                  'gender':'male'},
              1: {'id':'b',
                  'age':'12',
                  'name':'123',
                  'gender':'male'},
              2: {'id':'c',
                  'age':'12',
                  'name':'123',
                  'gender':'male'},
              3: {'id':'d',
                  'age':'12',
                  'name':'123',
                  'gender':'male'},
                  }
    print_valie_dict()

def print_menu_and_get_option():
    print('Menu')
    print('A. Вывести список пользователей')
    print('B. Посмотреть информацию о пользователе')
    print('C. Изменить данные о пользователе')
    print('D. Удалить выбранного пользователя')
    print('E. Добавить пользователя')
    print('F. Выход')          
    option = str(input('Inter your choice: '))
    clear_screen()
    return option

def process_option(option):
    if option == str('A'):
        list_user()
    elif option == str('B'):
        read_users()
    elif option == str('C'):
        edit_users()
    elif option == str('D'):
        delete()
    elif option == str('E'):
        create_user()
    elif option == str('F'):
        exit()
    clear_screen     
    return option
import os

def clear_screen():
    os.system('clear')

def list_user():
    print(dict.keys())

def read_users():
    print_valie_dict = input('Введите id пользователя:')
    print(dict.get(print_valie_dict))

def edit_users():
    dict[input('Введите id, которое хотите изменить')]
    print(dict)

def delete():
    delete_user = input('Введите id пользователя, которого хотите удалить:')
    print(dict.pop(delete_user))

def create_user():
    key = input('Введите id:')
    name = input('Введите Ваше имя')
    floor = input('Введите ваш пол:')
    age = input('Введите ваш возраст:')
    height = float(input('Введите Ваш рост, см'))
    weight = float(input('Введите ваш вес, кг:'))
    dict[key] = [name, floor, age, height, weight]
    print(dict)

def main():
    while option != 'q':
        option = print_menu_and_get_option()
        process_option(option)



