def decorator(foo):
    def wrapper(*args,**kwargs):
        try:
            res = foo(*args,**kwargs)
            return res
        except Exception as e:
            print(f'eroor: {e} , check your code')
            return None
    return wrapper


@decorator
def foo(x,y):
    return x + y

print(foo(4,))