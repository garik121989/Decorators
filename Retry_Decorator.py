import time
from functools import  wraps

def retry_decorator(retrie_number, delay, exception = Exception):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(1,retrie_number+1):
                try:
                    return func(*args,**kwargs)
                except exception as e:
                    print(f"Try {i} failed: {e}")
                    if i <= retrie_number:
                        print(f"retrying from {delay} seconds")
                        time.sleep(delay)

        return wrapper
    return decorator

@retry_decorator(retrie_number=3, delay= 1, exception = (TypeError,))
def func(x,y):
    return x + y

func(2,'j')




