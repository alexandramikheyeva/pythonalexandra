
def print_valie_dict():
    print(my_dict.get(input('Print key(id): ')))

    my_dict = {0:{'id':'a',
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
    print('1. Вывести список пользователей\n2: Посмотреть информацию\n3: Изменить данные\n4: Удалить пользователя\n5: Добавить пользователя')
    option = input('Inter your choice: ')
    clear_screen()
    return option

def process_option(option):
    if option == 1:
        list_user()
    elif option == 2:
        read_users()
    elif option == 3:
        edit_users()
    elif option == 4:
            delete_user()
    elif option == 5:
        create_user()
    clear_screen     
    return option
import os

def clear_screen():
    os.system('clear')

def list_user():
    print()
list_user()

def read_users():
    print()
read_users()

def edit_users():
    print()
edit_users()

def delete_user():
    print()
delete_user()

def create_user():
    print()
create_user()

def main():
    while option != 'q':
        option = print_menu_and_get_option()
        process_option(option)
        
if __name__ == '__main__':
   print_menu_and_get_option()
