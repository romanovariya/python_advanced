from functools import wraps


def reversed_dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        new_args = args[::-1]
        return func(*new_args, **kwargs)
    return inner
