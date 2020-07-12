import functools


def simple_decorator(func):
    @functools.wraps(func)
    def wrapper4(*args, **kwargs):
        print("Hey, I am decorator printing")
        func(*args, **kwargs)
    return wrapper4

@simple_decorator
def decorate_me(arg1, arg2):
    print(f"Hey, I am the original function with following arguments {arg1}, {arg2}")

a = decorate_me
a(2,4)
print(a.__name__)