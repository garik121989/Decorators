from functools import wraps

def authorization_decorator(allowed_ussers):
    def decorator(func):
        @wraps(func)
        def wrapper(user,*args,**kwargs):
            if user in allowed_ussers:
                return func(*args,**kwargs)
            else:
                print("Anauthorized user")
            raise PermissionError('You are not allowed')
        return wrapper
    return decorator


@authorization_decorator(["admin1","admin2"])
def func():
    print('Authorization')

try:
    func("admin3")
except PermissionError as e:
    print("Permision denied:", e)
