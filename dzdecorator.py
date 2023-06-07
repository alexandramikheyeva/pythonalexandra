def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        value = f'сумма счета:{func(*args, **kwargs)}'
        return value
    return wrapper_decorator
@decorator
def adds():
    return 2
login = input('Username:')
if login == 'admin':
    print(adds())
else:
    print('Доступ запрещен')