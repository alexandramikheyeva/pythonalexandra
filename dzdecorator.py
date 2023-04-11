def decorator(func):

    def wrapper_decorator(*args, **kwargs):

        value = func(*args, **kwargs)

        return value
    return wrapper_decorator