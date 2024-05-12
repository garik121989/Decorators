import time
from datetime import  datetime

def decorator(foo):
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        print(f'function starts at {datetime.now()}')
        res = foo(*args,**kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"function duration is {duration} seconds")
        print(f'function ends at {datetime.now()}')
        return res
    return wrapper


@decorator
def foo():
    time.sleep(5)

foo()
