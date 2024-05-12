from functools import wraps


def input_validation_decorator(foo):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if foo(*args,**kwargs):
                return func(*args,**kwargs)
            else:
                raise ValueError("not correct values")
        return wrapper
    return decorator


def foo(*args,**kwargs):
    for i in args:
        if not (isinstance(i, int) and i > 0):
            return False
    for key, value in kwargs.items():
        if not (isinstance(value, int) and value > 0):
            return False
    return True

@input_validation_decorator(foo)
def fn(x,y):
    return x + y


try:
    print(fn(4, 'd'))
except ValueError as e:
    print(e)


