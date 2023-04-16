
def print_valie_dict():
    print(my_dict.get(input('Print key(id): ')))

    my_dict = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
        }
    print_valie_dict()

def print_menu_and_get_option():
    print('A. Вывести список пользователей\nB: Посмотреть информацию\nC: Изменить данные\nD: Удалить пользователя\nE: Добавить пользователя')
    option = input('Inter your choice: ')
    while True:
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
    print({})
list_user()

def read_users():
    print({})
read_users()

def edit_users():
    print({})
edit_users()

def delete_user():
    print({})
delete_user()

def create_user():
    print({})
create_user()

def main():
    print_menu_and_get_option()
    list_user()

def main():
    print_menu_and_get_option()
    read_users()

def main():
    print_menu_and_get_option()
    edit_users()

def main():
    print_menu_and_get_option()
    delete_user()

def main():
    print_menu_and_get_option()
    create_user()
if __name__ == '__main__':
   print_menu_and_get_option()
