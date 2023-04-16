def clear_screen():
    pass
def list_users():
    pass
def create_user():
    pass
def print_menu_and_get_option():
    option = input('Inter your choice: ')
    clear_screen
    return option

def process_option(option):
    if option == 1:
        list_users()
    elif option == 2:
        create_user

def main():
    while option != 'q':
        option = print_menu_and_get_option
        process_option(option)
if __name__ == '__main__':
    main()
