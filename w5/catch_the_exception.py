def exception_logger(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print('ZeroDivisionError')
        except ArithmeticError:
            print('ArithmeticError')
        except AssertionError:
            print('AssertionError')

    return inner
