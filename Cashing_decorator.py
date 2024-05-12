from functools import wraps

def decorator(foo):
    cash = {}
    @wraps(foo)
    def wrapper(*args,**kwargs):
        key = (args,frozenset(kwargs.items()))
        print(key)
        if key not in cash:
            cash[key] = foo(*args,**kwargs)
        return cash[key]
    return wrapper



@decorator
def fac(n):
    return 1 if n == 0 else  (n * fac(n-1))


print(fac(5))