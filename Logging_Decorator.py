import time
from functools import wraps
import logging

def decorator(foo):

    @wraps(foo)
    def wrapper(*args,**kwargs):
        try:
            start = time.perf_counter()
            res = foo(*args,**kwargs)
            end = time.perf_counter() - start
            print(f"function duration is {end} seconds")
            return res
        except Exception as e:
              print(f'function failed {e}')
              return None


    return wrapper

@decorator
def foo(x,y):
    return x + y

foo(4,'hggj')